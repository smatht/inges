from django.contrib import admin

from pedidos.models import OrdenRetiro_detalle, OrdenRetiro_cabecera


class ORDetInline(admin.TabularInline):
  model = OrdenRetiro_detalle
  extra = 1


class ORCabAdmin(admin.ModelAdmin):
  inlines = [ORDetInline]

admin.site.register(OrdenRetiro_cabecera, ORCabAdmin)