from facturacion.models import *
from facturacion.forms import Factura_recibida
from django.contrib.sites.models import Site
from django.contrib import admin
from actions import export_as_csv
import decimal


# Esta clase modifica la visualizacion del modelo en el admin, en este caso
# muestra los campos emisor, fecha y factura en la visualizacion de los
# campos dela tabla (list_display).
# Tambien con list_filter colocamos un filtro.
class Factura_recibida_admin(admin.ModelAdmin):
	# form = Factura_recibida
	list_display = ('emisor', 'fecha', 'nro_factura', 'valor_subtotal', 'valor_iva', 'percepciones_otros', 'valor_total')
	list_filter = ('iva', 'fecha', 'registrado_el')
	#search_fields = ('iva__porcentaje',)
	search_fields = ('emisor__nombre', 'nro_factura',)
	# Para editar un campo de forma inline
	#list_editable = ('percepciones_otros',)
	# Agregar busqueda optimizada
	# raw_id_fields = ('emisor',)
	actions = [export_as_csv]
	fieldsets = (
        (None, {
            'fields': ('registrado_el', 'fecha', 'emisor', 'nro_factura', 'subtotal', 'iva', 'percepciones_otros')
        }),
    )
	
	# Para mostrar una imagen en un campo
	# def valor_iva(self, obj):
	# 	url = obj.valor_iva_imagen()
	# 	# tag = '<img src="%s" />' % url
	# 	tag = url
	# 	return tag
	# valor_iva.allow_tags = True

	def valor_iva(self, obj):
		iva = obj.impuesto()
		porc = obj.iva.porcentaje
		badge = 'badge badge-success'
		if porc == 21:
			porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
		elif porc == 0:
			badge = 'badge'
			porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
		elif porc == 10.5:
			badge = 'badge badge-info'
			porc = decimal.Decimal(round(porc, 1)).normalize()
		elif porc == 27:
			porc = '&nbsp;'+str(decimal.Decimal(round(porc, 1)).normalize())+'&nbsp;&nbsp;'
			badge = 'badge badge-warning'
		
		return '$%s <span class="%s pull-right">%s%%</span>' % (round(iva, 2), badge, porc)
	valor_iva.allow_tags = True

	def valor_total(self, obj):
		total = obj.total()
		return "$"+str(round(total, 2))

	def valor_subtotal(self, obj):
		subtotal = obj.subtotal
		return "$"+str(round(subtotal, 2))

	

	

# Sirve para poder agregar facturas inline cuando se agrega un registro
# de un campo relacionado por clave foranea #
# class Factura_recibida_inline(admin.StackedInline):
# 	model = Factura_recibida
# 	extra = 1


# class Albaran_recibido_inline(admin.StackedInline):
# 	model = Albaran_recibido
# 	extra = 1


class Factura_emitida_admin(admin.ModelAdmin):
	# form = Factura
	# list_display = ('ente', 'fecha', 'total', 'impuesto')

	list_filter = ('fecha',)
	fieldsets = (
        (None, {
            'fields': ('registrado_el', 'fecha', 'nro_factura', 'ente', 'iva', 'total','percepciones_otros')
        }),
        )
	actions = [export_as_csv]


class Albaran_recibido_admin(admin.ModelAdmin):
	# form = Factura
	list_display = ('emisor', 'fecha', 'total')
	search_fields = ('emisor__nombre', 'nro_albaran',)
	list_filter = ('fecha', 'registrado_el')
	actions = [export_as_csv]
	fieldsets = (
        (None, {
            'fields': ('registrado_el', 'fecha', 'emisor', 'nro_albaran', 'total')
        }),
    )


class Empresa_Ente_admin(admin.ModelAdmin):
	list_display = ('nombre', 'cuit','direccion', 'telefono')
	search_fields = ('nombre',)
	# ordering = ['nombre']
	actions = [export_as_csv]
	# inlines = [ Factura_recibida_inline, Albaran_recibido_inline]

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


admin.site.register(Factura_recibida, Factura_recibida_admin)
admin.site.register(Factura_emitida, Factura_emitida_admin)
admin.site.register(Albaran_emitido, HideAdmin)
admin.site.register(Albaran_recibido, Albaran_recibido_admin)
admin.site.register(Iva)
admin.site.register(Empresa_Ente, Empresa_Ente_admin)
admin.site.register(Pais, HideAdmin)
admin.site.register(Ciudad, HideAdmin)
admin.site.register(Localidad, HideAdmin)
admin.site.unregister(Site)