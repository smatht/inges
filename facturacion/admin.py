from facturacion.models import *
from django.contrib.sites.models import Site
from django.contrib import admin
from actions import export_as_csv


# Esta clase modifica la visualizacion del modelo en el admin, en este caso
# muestra los campos emisor, fecha y factura en la visualizacion de los
# campos dela tabla (list_display).
# Tambien con list_filter colocamos un filtro.
class Factura_recibida_admin(admin.ModelAdmin):
	list_display = ('emisor', 'fecha', 'nro_factura', 'neto', 'valor_iva', 'percepciones_otros', 'total')
	list_filter = ('iva', 'registrado_el', 'registrado_el')
	#search_fields = ('iva__porcentaje',)
	search_fields = ('nro_factura',)
	# Para editar un campo de forma inline
	list_editable = ('percepciones_otros',)
	# Agregar busqueda optimizada
	# raw_id_fields = ('emisor',)
	actions = [export_as_csv]
	
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
		badge = 'success'
		if porc == 0:
			badge = 'info'
		
		return '$%s <span class="badge badge-%s pull-right">%s%%</span>' % (iva, badge, porc)
	valor_iva.allow_tags = True

	def total(self, obj):
		resultado = obj.neto + obj.impuesto() + obj.percepciones_otros
		return "%.2f" % resultado

	

# Sirve para poder agregar facturas inline cuando se agrega un registro
# de un campo relacionado por clave foranea #
# class Factura_recibida_inline(admin.StackedInline):
# model = Factura_recibida
# extra = 1

class Factura_emitida_admin(admin.ModelAdmin):
	list_display = ('ente', 'fecha', 'neto_iva', 'iva')
	list_filter = ('fecha',)
	actions = [export_as_csv]

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
admin.site.register(Iva, HideAdmin)
admin.site.register(Empresa)
admin.site.register(Ente)
admin.site.register(Pais, HideAdmin)
admin.site.register(Ciudad, HideAdmin)
admin.site.register(Localidad, HideAdmin)
admin.site.unregister(Site)