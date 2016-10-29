from django.contrib import admin

from actions import export_OR_as_pdf, save_then_pdf
from pedidos.models import OrdenRetiro_detalle, OrdenRetiro_cabecera


class ORDetInline(admin.TabularInline):
  model = OrdenRetiro_detalle
  extra = 1


class ORCabAdmin(admin.ModelAdmin):
  list_display = ('id', 'fecha', 'proveedor', 'destino', 'remitente')
  exclude = ('remitente', )
  inlines = [ORDetInline]
  actions = [export_OR_as_pdf]

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'remitente', None) is None:
      obj.remitente = request.user
    obj.save()
    save_then_pdf(request, obj)


admin.site.register(OrdenRetiro_cabecera, ORCabAdmin)