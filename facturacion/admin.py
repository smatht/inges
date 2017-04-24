from facturacion.models import *
from facturacion.forms import FacturaForm, FacturaDetalleForm
from django.contrib.sites.models import Site
from django.contrib import admin
from actions import export_as_csv
import decimal


class Registro_admin(admin.ModelAdmin):
    list_display = ('cuit', 'razon_social')
    fieldsets = (
        (None, {
            'fields': ('cuit', 'razon_social', 'nombre_fantasia', 'domicilio_comercial', 'domicilio_fiscal', 'telefono', 'telefono_secundario', 'email', 'iva', 'fecha_inicio_actividad', 'membrete', 'logo', 'pais', 'ciudad', 'localidad')
        }),
    )

# Mediante esta clase podremos mostrar el formulario de detalle de factura
# al momento de generar la factura
class FacturaDetalleInline(admin.TabularInline):
  model = Factura_detalle
  form = FacturaDetalleForm
  extra = 2

class FacturaDetalleAdmin(admin.ModelAdmin):
    form = FacturaDetalleForm

# Esta clase modifica la visualizacion del modelo en el admin, en este caso
# muestra los campos emisor, fecha y factura en la visualizacion de los
# campos de la tabla (list_display).
# Tambien con list_filter colocamos un filtro.
class Registro_factura_admin(admin.ModelAdmin):
  form = FacturaForm
  list_display = ('emisor', 'fecha_factura', 'nro_factura', 'valor_subtotal', 'valor_iva', 'valor_total')
  exclude = ('usuario',)
  list_filter = ('fecha_factura', 'fecha_registro')
  #search_fields = ('iva__porcentaje',)
  search_fields = ('emisor__razon_social', 'nro_factura',)
  # Para editar un campo de forma inline
  #list_editable = ('percepciones_otros',)
  # Agregar busqueda optimizada
  # raw_id_fields = ('emisor',)
  inlines = [FacturaDetalleInline]
  actions = [export_as_csv]

  fieldsets = (
        (None, {
            'fields': ('fecha_registro', 'fecha_factura', 'registro', 'emisor', 'nro_factura', 'tipo', 'pagado', 'esCopia', 'observaciones')
        }),
    )

  def save_model(self, request, obj, form, change):
    if getattr(obj, 'usuario', None) is None:
      obj.usuario = request.user
    obj.save()

  def suit_row_attributes(self, obj, request):
    pagado = {1: '', 0: 'warning'}.get(obj.pagado)
    copia = {1: 'error', 0: ''}.get(obj.esCopia)
    if copia:
      return {'class': copia}
    if pagado:
      return {'class': pagado}

  # Para mostrar una imagen en un campo
  # def valor_iva(self, obj):
  # 	url = obj.valor_iva_imagen()
  # 	# tag = '<img src="%s" />' % url
  # 	tag = url
  # 	return tag
  # valor_iva.allow_tags = True

  def valor_iva(self, obj):

    iva = obj.impuesto()
    # porc = obj.iva.porcentaje
    # badge = 'badge badge-success'
    # if porc == 21:
    #   porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
    # elif porc == 0:
    #   badge = 'badge'
    #   porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
    # elif porc == 10.5:
    #   badge = 'badge badge-info'
    #   porc = decimal.Decimal(round(porc, 1)).normalize()
    # elif porc == 27:
    #   porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
    #   badge = 'badge badge-warning'
    # return '$%s <span class="%s pull-right">%s%%</span>' % (round(iva, 2), badge, porc)
    return '$%s' % round(iva, 2)
  valor_iva.allow_tags = True

  def valor_total(self, obj):
    total = obj.total()
    return "$"+str(round(total, 2))

  def valor_subtotal(self, obj):
    subtotal = obj.subtotal()
    return "$"+str(round(subtotal, 2))





# Sirve para poder agregar facturas inline cuando se agrega un registro
# de un campo relacionado por clave foranea #
# class Registro_factura_inline(admin.StackedInline):
# 	model = Registro_factura
# 	extra = 1


# class Recibo_inline(admin.StackedInline):
# 	model = Recibo
# 	extra = 1


class Emision_factura_admin(admin.ModelAdmin):
  # form = Factura
  # list_display = ('ente', 'fecha', 'total', 'impuesto')
  form = FacturaForm
  list_filter = ('fecha_factura',)
  fieldsets = (
        (None, {
            'fields': ('fecha_registro', 'fecha_factura', 'nro_factura', 'cliente', 'iva', 'total','percepciones_otros', 'detalle')
        }),
        )
  actions = [export_as_csv]


class Recibo_admin(admin.ModelAdmin):
  # form = Factura
  list_display = ('emisor', 'fecha_recibo', 'total')
  search_fields = ('emisor__razon_social', 'nro_recibo',)
  list_filter = ('fecha_recibo', 'fecha_registro')
  actions = [export_as_csv]
  fieldsets = (
        (None, {
            'fields': ('fecha_registro', 'fecha_recibo', 'emisor', 'nro_recibo', 'total', 'detalle')
        }),
    )


# class Empresa_Ente_admin(admin.ModelAdmin):
# 	list_display = ('nombre', 'cuit','direccion', 'telefono')
# 	search_fields = ('nombre',)
# 	# ordering = ['nombre']
# 	actions = [export_as_csv]
# 	# inlines = [ Registro_factura_inline, Recibo_inline]

class Proveedor_admin(admin.ModelAdmin):
  list_display = ('razon_social', 'cuit','domicilio_comercial', 'telefono')
  search_fields = ('razon_social',)
  actions = [export_as_csv]
  fieldsets = (
        (None, {
            'fields': ('razon_social', 'cuit', 'domicilio_comercial', 'email', 'sitio_web', 'telefono', 'telefono_secundario', 'pais', 'ciudad', 'localidad')
        }),
    )

class Cliente_admin(admin.ModelAdmin):
  list_display = ('nombre', 'dni','domicilio_fiscal', 'telefono')
  search_fields = ('nombre',)
  actions = [export_as_csv]
  fieldsets = (
        (None, {
            'fields': ('nombre', 'dni', 'cuil', 'domicilio_fiscal', 'email', 'telefono', 'telefono_secundario', 'pais', 'ciudad', 'localidad')
        }),
    )

# Para facilitar el agregado de Many To Many Field se hace esto...
# class Campo_many_to_many_admin(admin.ModelAdmin):
  # filter_horizontal = ('campo_de_la_relacion',)
# Otra forma
# filter_vertical = ('campo_de_la_relacion',)

class HideAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Factura_detalle, FacturaDetalleAdmin)
admin.site.register(Registro, Registro_admin)
admin.site.register(Registro_factura, Registro_factura_admin)
admin.site.register(Emision_factura, Emision_factura_admin)
# admin.site.register(Albaran_emitido, HideAdmin)
admin.site.register(Recibo, Recibo_admin)
admin.site.register(Proveedor, Proveedor_admin)
admin.site.register(Cliente, Cliente_admin)
admin.site.register(Iva)
# admin.site.register(Empresa_Ente, Empresa_Ente_admin)
admin.site.register(Pais, HideAdmin)
admin.site.register(Ciudad, HideAdmin)
admin.site.register(Localidad, HideAdmin)
admin.site.unregister(Site)