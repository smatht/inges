import datetime
from django.contrib import admin, messages
from django.db.models import Q
from django.forms import SelectMultiple
from django.db import models

# Register your models here.
from django.shortcuts import redirect

from forms import FondosForm, CajaForm
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
    form = FondosForm
    list_display = ('empresa', 'fPago', 'proveedor', 'importe')
    list_filter = ('empresa', 'proveedor')
    exclude = ('fCarga', 'operador', 'anulado', 'aplicado')
    filter_horizontal = ('facturas',)
    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-facturas',),
            'fields': ('empresa', 'proveedor', 'fPago', 'facturas'),
        }),
        ('Efectivo', {
            'classes': ('suit-tab', 'suit-tab-valores',),
            'fields': ('caja', 'importe', 'comentario'),
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

    def render_change_form(self, request, context, *args, **kwargs):
        # Busca ids de facturas ya pagadas (asignadas a un recibo)
        idPagadas = OrdenPago.facturas.through.objects.values_list('compra', flat=True)
        context['adminform'].form.fields['empresa'].initial = Configuracion.objects.get(pk=1).empresa
        context['adminform'].form.fields['facturas'].queryset = Compra.objects.filter(~Q(id__in=idPagadas), condPago='CRE')
        return super(OrdenPagoAdmin, self).render_change_form(request, context, args, kwargs)

    # def save_model(self, request, obj, form, change):
    #     print(form.diferencia)
    #     if getattr(obj, 'diferencia', None) is not 0:
    #         messages.add_message(request, messages.ERROR, 'ERROR EN LA OPERACION')
    #         print(messages.get_messages(request))
    #     else:
    #         obj.save()


@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    form = CajaForm
    list_display = ('tipoCaja', 'fApertura', 'destino', 'montoInicial', 'acumEntradas', 'acumSalidas', 'saldo')
    # list_filter = ('caja__destino',)
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



admin.site.register(TipoCaja)
admin.site.register(TipoMovCaja)
