from django.contrib import admin, messages

# Register your models here.
from django_extensions.admin import ForeignKeyAutocompleteAdmin
from stock.models import Producto, Familia, Linea, Unidades

from stock.forms import ProductoForm


@admin.register(Producto)
class ProductoAdmin(ForeignKeyAutocompleteAdmin):
    form = ProductoForm
    list_display = ('id', 'descripcion', 'activo', 'familia', 'precio')
    search_fields = ('descripcion',)
    filter_horizontal = ('proveedor',)

    def save_model(self, request, obj, form, change):
        print(form.changed_data)
        print(form.cleaned_data['descripcionCorta'])
        print(obj.descripcionCorta)
        if 'descripcionCorta' in form.changed_data:
            messages.success(request, "Se cambio descripcion corta")
        obj.save()




admin.site.register(Familia)
admin.site.register(Linea)
admin.site.register(Unidades)