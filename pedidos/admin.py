from django.contrib import admin

from pedidos.forms import OrdenRetiroForm
from pedidos.models import OrdenRetiro_detalle, OrdenRetiro_cabecera


class ORDetInline(admin.TabularInline):
  model = OrdenRetiro_detalle
  extra = 1


class ORCabAdmin(admin.ModelAdmin):
  list_display = ('id', 'fecha', 'proveedor', 'destino', 'remitente')
  exclude = ('remitente', )
  inlines = [ORDetInline]

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    obj.save()


admin.site.register(OrdenRetiro_cabecera, ORCabAdmin)