from django.contrib import admin, messages
from django.db.models import Q
from django.forms import SelectMultiple
from django.db import models

# Register your models here.
from forms import FondosForm
from mantenimiento.models import Configuracion

from compras.models import Compra
from models import TipoCaja, MovCaja, TipoMovCaja, OrdenPago, Caja


@admin.register(MovCaja)
class MovCajaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'obra', 'importe', 'tipoMovCaja', 'descripcion')
    list_filter = ('caja__destino',)

    def obra(self, obj):
        return obj.caja.destino



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
    #     pass
    #     if getattr(obj, 'diferencia', None) is not 0:
    #         messages.add_message(request, messages.ERROR, 'ERROR EN LA OPERACION')
    #         pass
    #     else:
    #         obj.save()


@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('fecha', 'obra', 'importe', 'tipoMovCaja', 'descripcion')
    # list_filter = ('caja__destino',)


admin.site.register(TipoCaja)
admin.site.register(TipoMovCaja)
