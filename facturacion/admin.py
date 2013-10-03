from facturacion.models import Factura_recibida, Iva, Empresa
from django.contrib import admin
from actions import export_as_csv

# Esta clase modifica la visualizacion del modelo en el admin, en este caso
# muestra los campos emisor, fecha y factura en la visualizacion de los
# campos dela tabla (list_display). 
# Tambien con list_filter colocamos un filtro.
class Factura_recibida_admin(admin.ModelAdmin):
	list_display = ('emisor', 'fecha', 'neto', 'valor_iva', 'percepciones_otros', 'total')
	list_filter = ('emisor', 'fecha')
	#search_fields = ('iva__porcentaje',)
	search_fields = ('nro_factura', 'fecha')
	# list_editable = ('fecha', 'neto', 'percepciones_otros')
	actions = [export_as_csv]
	def valor_iva(self, obj):
		url = obj.valor_iva_imagen()
		tag = '<img src="%s" />' % url
		return tag
	valor_iva.allow_tags = True

	def total(self, obj):
		resultado = obj.neto + obj.impuesto() + obj.percepciones_otros
		return "%.2f" % resultado

admin.site.register(Factura_recibida, Factura_recibida_admin)
admin.site.register(Iva)
admin.site.register(Empresa)