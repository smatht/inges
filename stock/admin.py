from django.contrib import admin

# Register your models here.
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from stock.models import Producto, Familia, Linea, Unidades

from stock.forms import ProductoForm


@admin.register(Producto)
class ProductoAdmin(ForeignKeyAutocompleteAdmin):
    form = ProductoForm
    list_display = ('id', 'descripcion', 'activo', 'familia')
    search_fields = ('descripcion',)



admin.site.register(Familia)
admin.site.register(Linea)
admin.site.register(Unidades)