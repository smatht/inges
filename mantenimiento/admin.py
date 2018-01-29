from django.contrib import admin

from models import TiposDoc, Impuesto

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


# Register your models here.
