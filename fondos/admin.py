import datetime

from django.conf.urls import url
from django.contrib import admin, messages
from functools32 import update_wrapper

from fondos.reports import orden_pago_as_pdf
from fondos.utils import getOrOpenCaja
from fondos_externos.models import Cuenta
from forms import OPForm, CajaForm
from mantenimiento.models import Configuracion

from compras.models import Compra, DocCuentaProveedor
from models import TipoCaja, MovCaja, OrdenPago, Caja, PagosProveedor


@admin.register(MovCaja)
class MovCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'tipoCaja', 'obra', 'importe', 'tipoMovCaja', 'descripcion', 'operacion')
    list_filter = ('caja__destino', 'caja__tipoCaja')
    fieldsets = (
        (None, {
            'fields': ('empresa', 'caja', 'tipoMovCaja', 'descripcion', 'importe'),
        }),
        ('Datos adicionales:', {
            'classes': ('collapse',),
            'fields': ('fecha', 'tipoDoc', 'numDoc', 'proveedor')}),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'operador', None) is None:
            obj.operador = request.user
        #     # messages.add_message(request, messages.INFO, 'Operador registrado')
        # if getattr(obj, 'fecha', None) is None:
        #     obj.fecha = datetime.datetime.now
        # if getattr(obj, 'tipoMovCaja').suma:
        #     obj.caja.acumEntradas += obj.importe
        # else:
        #     obj.caja.acumSalidas += obj.importe
        #
        # obj.caja.save()
        obj.save()

    def render_change_form(self, request, context, *args, **kwargs):
        # context['adminform'].form.fields['tipoDoc'].queryset = TiposDoc.objects.filter(tipo=1)
        context['adminform'].form.fields['empresa'].initial = Configuracion.objects.get(pk=1).empresa
        return super(MovCajaAdmin, self).render_change_form(request, context, args, kwargs)

    def obra(self, obj):
        return obj.caja.destino

    def tipoCaja(self, obj):
        return obj.caja.tipoCaja

    def operacion(self, obj):
        if (obj.tipoMovCaja.suma):
            return '<img src="/static/admin/img/ing.png" alt="True">'
        else:
            return '<img src="/static/admin/img/egre.png" alt="False">'
    operacion.allow_tags = True



@admin.register(OrdenPago)
class OrdenPagoAdmin(admin.ModelAdmin):
    form = OPForm
    list_display = ('empresa', 'fPago', 'beneficiario', 'importe', 'acciones')
    list_filter = ('empresa', 'proveedor')
    exclude = ('fCarga', 'operador', 'anulado', 'aplicado')
    filter_horizontal = ('facturas',)
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-facturas',),
            'fields': ('empresa', 'proveedor', 'personal', ('fPago', 'tipoPago'), 'facturas'),
        }),
        ('Efectivo', {
            'classes': ('suit-tab', 'suit-tab-valores',),
            'fields': ('tipoCaja', 'obra', 'importe'),
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-valores',),
            'fields': (('motivo', 'imprimir_recibo'), 'comentario'),
        }),
        ('Cheques propios', {
            'classes': ('suit-tab', 'suit-tab-valores', 'collapse'),
            'fields': [],
        }),
        ('Transferencia bancaria', {
            'classes': ('suit-tab', 'suit-tab-valores', 'collapse'),
            'fields': [],
        }),
        ('Datos del pago', {
            'classes': ('suit-tab', 'suit-tab-valores',),
            'fields': ['total_valores', 'total_a_pagar', 'diferencia']}),
    )
    suit_form_tabs = (('facturas', 'Facturas a pagar'), ('valores', 'Valores'))

    def wrap(self, view):
        def wrapper(*args, **kwargs):
            return self.admin_site.admin_view(view)(*args, **kwargs)

        wrapper.model_admin = self
        return update_wrapper(wrapper, view)

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['empresa'].initial = Configuracion.objects.get(pk=1).empresa
        context['adminform'].form.fields['facturas'].queryset = Compra.objects.filter(fSaldada=None)
        context['adminform'].form.fields['motivo'].initial = Configuracion.objects.get(pk=1).fondos_orden_pago_movimiento
        if kwargs.get('change'):
            if kwargs.get('obj').caja:
                tc = kwargs.get('obj').caja.tipoCaja
                oc = kwargs.get('obj').caja.destino
                context['adminform'].form.fields['tipoCaja'].initial = tc
                context['adminform'].form.fields['obra'].initial = oc
        return super(OrdenPagoAdmin, self).render_change_form(request, context, args, kwargs)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['tipoCaja'] is not None:
            if form.cleaned_data['obra'] is not None:
                obj.caja = getOrOpenCaja(form.cleaned_data['tipoCaja'], form.cleaned_data['obra'])
        obj.save()

    def beneficiario(self, obj):
        if obj.proveedor:
            return obj.proveedor
        else:
            return obj.personal.last_name + ', ' + obj.personal.first_name

    def imprimirOrden(self, request, orden_id, *args, **kwargs):
        qs = OrdenPago.objects.get(pk=orden_id)
        return orden_pago_as_pdf(request, qs)

    def get_urls(self):
        urls = super(OrdenPagoAdmin, self).get_urls()
        custom_urls = [
            url(
                r'^(?P<orden_id>.+)/deposit/$',
                self.admin_site.admin_view(self.imprimirOrden),
                name='imprimirOrden',
            ),
        ]
        return custom_urls + urls

    # Los siguientes 3 metodos sirven para Operar con la OP una vez guardada
    def response_add(self, request, new_object, **kwargs):
        obj = self.despues_guardar_orden_pago(request, new_object)
        return super(OrdenPagoAdmin, self).response_add(request, obj)

    def response_change(self, request, obj):
        obj = self.despues_guardar_orden_pago(request, obj)
        return super(OrdenPagoAdmin, self).response_change(request, obj)

    def despues_guardar_orden_pago(self, request, op):
        # Modifica saldos de facturas implicadas (si las hubiere)
        facturas = op.facturas.all()
        if facturas.count() > 0:
            saldoTotal = 0
            # Importe dividido entre cantidad de facturas a pagar
            imp_div = op.importe / facturas.count()
            for factura in facturas:
                nroPago = PagosProveedor.objects.filter(documento=factura).count()
                p = PagosProveedor(documento=factura, nroPago=nroPago+1, fPago=datetime.datetime.now,
                                   importe=imp_div, ordenPago=op)
                dc = DocCuentaProveedor.objects.get(documento=factura)
                dc.importePagado += imp_div
                dc.importeSaldo -= imp_div
                if dc.importeSaldo <= 0.1:
                    factura.fSaldada = datetime.datetime.now()
                    factura.save()
                p.save()
                dc.save()
            op.facturas = []
            op.save()

        # Realizamos movimiento de caja
        caja = getattr(op, 'caja', None)

        if caja is not None:
            if getattr(op, 'proveedor', None) is not None:
                benef = op.proveedor
            else:
                benef = op.personal
            desc = "Orden de pago: %s. Beneficiario: %s" % (op.motivo, benef)
            m = MovCaja(caja=caja, empresa=op.empresa, descripcion=desc, operador=request.user,
                        importe=op.importe, tipoMovCaja=op.motivo)
            m.save()
        return op


@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    form = CajaForm
    list_display = ('tipoCaja', 'destino', 'fApertura', 'montoInicial', 'acumEntradas', 'acumSalidas', 'saldo')
    # list_filter = ('caja__destino',)
    ordering = ['-fCierre', '-fApertura']
    fieldsets = (
        (None, {
            'fields': ('tipoCaja', 'destino', 'montoInicial'),
        }),
        ('Vinculaciones externas:', {
            'classes': ('collapse',),
            'fields': ['cuentaWallet']}),
    )

    def saldo(self, obj):
        return obj.montoInicial + obj.acumEntradas - obj.acumSalidas

    # def render_change_form(self, request, context, *args, **kwargs):
    #     context['adminform'].form.fields['cuentaWallet'].queryset = Cuenta.objects.all()
    #     return super(CajaAdmin, self).render_change_form(request, context, args, kwargs)

    def save_model(self, request, obj, form, change):
        cuenta = form.cleaned_data['cuentaWallet']
        if cuenta is not None:
            obj.idCuentaWallet = cuenta.id
            obj.nombreCuentaWallet = cuenta.name
        else:
            obj.idCuentaWallet = ''
            obj.nombreCuentaWallet = ''
        obj.save()

    def suit_row_attributes(self, obj, request):
        fila = ''
        if obj.fCierre == None:
            fila = 'info'
        if fila != '':
            return {'class': fila}

    def render_change_form(self, request, context, *args, **kwargs):
        if kwargs.get('change'):
            if kwargs.get('obj'):
                idW = kwargs.get('obj').idCuentaWallet
                cuenta = Cuenta.objects.get(pk=idW)
                context['adminform'].form.fields['cuentaWallet'].initial = cuenta
        return super(CajaAdmin, self).render_change_form(request, context, args, kwargs)



admin.site.register(TipoCaja)

