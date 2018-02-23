from django.contrib import admin
from django.shortcuts import redirect

from models import TiposDoc, Impuesto, Configuracion


@admin.register(TiposDoc)
class TiposDocAdmin(admin.ModelAdmin):
    radio_fields = {"aplicaStock": admin.VERTICAL}
    fieldsets = [
        (None, {'fields': ['id', 'descripcion', 'esFactura', 'tipo', 'aplicaStock']}),
    ]


@admin.register(Impuesto)
class ImpuestoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['descripcion', 'tipoImpuesto', 'valorImpuesto', 'esPorcentaje', 'esObligatorio']}),
    ]


@admin.register(Configuracion)
class ConfigAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['empresa']}),
        (None, {
            'classes': ('suit-tab suit-tab-compras',),
            'fields': ['compras_tipoDoc', 'compras_condPago', 'compras_usaPrFinal',
                       'compras_FacAfectaStk']}),
        (None, {
            'classes': ('suit-tab suit-tab-ventas',),
            'fields': ['ventas_tipoDoc']}),
    ]
    suit_form_tabs = (('general', 'General'),('compras', 'Compras'), ('ventas', 'Ventas'))

    def response_add(self, request, new_object, **kwargs):
        return redirect('/administracion/')

    def response_change(self, request, obj):
        return redirect('/administracion/')


# Register your models here.
