from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models

# Register your models here.
from forms import FondosForm
from mantenimiento.models import Configuracion

from compras.models import Compra
from models import TipoCaja, MovCaja, TipoMovCaja, OrdenPago


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

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['empresa'].initial = Configuracion.objects.get(pk=1).empresa
        context['adminform'].form.fields['facturas'].queryset = Compra.objects.filter(condPago='CRE')
        return super(OrdenPagoAdmin, self).render_change_form(request, context, args, kwargs)



admin.site.register(TipoCaja)
admin.site.register(TipoMovCaja)
