from django.contrib import admin

# Register your models here.
from stock.models import Producto, Familia, Linea, Unidades


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'activo', 'familia')



admin.site.register(Familia)
admin.site.register(Linea)
admin.site.register(Unidades)