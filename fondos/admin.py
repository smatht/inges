import datetime

from django.conf.urls import url
from django.contrib import admin, messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.forms import SelectMultiple
from django.db import models
from django.utils.safestring import mark_safe
# Register your models here.
from django.shortcuts import redirect
from functools32 import update_wrapper

from fondos.reports import orden_pago_as_pdf
from fondos.utils import getOrOpenCaja
from forms import OPForm, CajaForm
from mantenimiento.models import Configuracion

from compras.models import Compra

from fondos_externos.models import Cuenta
from models import TipoCaja, MovCaja, TipoMovCaja, OrdenPago, Caja


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
            'fields': ('empresa', 'proveedor', 'personal', 'fPago', 'facturas'),
        }),
        ('Efectivo', {
            'classes': ('suit-tab', 'suit-tab-valores',),
            'fields': ('tipoCaja', 'obra', 'importe', 'comentario'),
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
            'fields': [('total_valores', 'imprimir_recibo'), 'total_a_pagar', 'diferencia']}),
    )
    suit_form_tabs = (('facturas', 'Facturas a pagar'), ('valores', 'Valores'))

    def wrap(self, view):
        def wrapper(*args, **kwargs):
            return self.admin_site.admin_view(view)(*args, **kwargs)

        wrapper.model_admin = self
        return update_wrapper(wrapper, view)

    def render_change_form(self, request, context, *args, **kwargs):
        # Busca ids de facturas ya pagadas (asignadas a un recibo)
        idPagadas = OrdenPago.facturas.through.objects.values_list('compra', flat=True)
        context['adminform'].form.fields['empresa'].initial = Configuracion.objects.get(pk=1).empresa
        context['adminform'].form.fields['facturas'].queryset = Compra.objects.filter(~Q(id__in=idPagadas), condPago='CRE')
        if kwargs.get('change'):
            if kwargs.get('obj').caja:
                tc = kwargs.get('obj').caja.tipoCaja
                oc = kwargs.get('obj').caja.destino
                context['adminform'].form.fields['tipoCaja'].initial = tc
                context['adminform'].form.fields['obra'].initial = oc
        return super(OrdenPagoAdmin, self).render_change_form(request, context, args, kwargs)

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['tipoCaja'] is not None:
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



admin.site.register(TipoCaja)
admin.site.register(TipoMovCaja)
