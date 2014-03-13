# encoding:utf-8
from django.db import models
#from django.contrib.auth.models import User
import datetime

############################################
#     Clases secundarias Facturacion       #
############################################
class Iva(models.Model):
	porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return unicode(self.porcentaje)


class Pais(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.nombre)


class Ciudad(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return unicode(self.nombre)


class Localidad(models.Model):
	nombre = models.CharField(max_length=50)
	ciudad = models.ForeignKey(Ciudad)

	def __unicode__(self):
		return unicode(self.nombre)


class Empresa_Ente(models.Model):
	nombre = models.CharField(max_length=75)
	cuit = models.CharField(max_length=20, blank=True)
	direccion = models.CharField(max_length=140, blank=True)
	telefono = models.CharField(max_length=50, blank=True)
	telefono_secundario = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	sitio_web = models.CharField(max_length=140, blank=True)
	pais = models.ForeignKey(Pais, blank=True, null=True)
	ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
	localidad = models.ForeignKey(Localidad, blank=True, null=True)

	class Meta:
           ordering = ['nombre']

	def __unicode__(self):
		return unicode(self.nombre)



############################################
#     Clases principales Facturacion       #
############################################
class Factura(models.Model):
	registrado_el = models.DateField(default=datetime.datetime.now, 
		help_text="Cambie este campo sólo en caso de registrar una factura para un mes anterior, tenga en cuenta que al registrar para otro mes ésta no se incluirá en los informes del mes actual.")
	fecha = models.DateField()
	nro_factura = models.CharField(max_length=15)
	subtotal = models.DecimalField(max_digits=10, decimal_places=2)
	iva = models.ForeignKey(Iva)
	percepciones_otros = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def impuesto(self):
		resultado = (self.iva.porcentaje * self.subtotal)/100
		return resultado

	def total(self):
		resultado = (self.subtotal + self.impuesto() + self.percepciones_otros)
		return resultado

	class Meta:
		abstract = True


class Factura_recibida(Factura):
	emisor = models.ForeignKey(Empresa_Ente)
	# Para registrar al usuario que agrega el registro
	# usuario = models.ForeignKey(User)

	# Para saberla fecha y hora de ingreso del registro
	# timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return unicode(self.fecha)+" - "+self.nro_factura

	# Para enviar una imagen al admin
	# def valor_iva_imagen(self):
	# 	resultado = (self.iva.porcentaje * self.neto)/100
	# 	if self.iva.porcentaje == 21:
	# 		return '<img src="http://placehold.it/80x40/2ECC5F/ffffff/&text=$+%.2f" title= "21%%" />' % resultado
	# 	elif self.iva.porcentaje == 10.5:
	# 		return '<img src="http://placehold.it/80x40/FF8753/ffffff/&text=$+%.2f" title= "10,5%%" />' % resultado
	# 	elif self.iva.porcentaje == 27:
	# 		return '<img src="http://placehold.it/80x40/5E7699/ffffff/&text=$+%.2f" title= "27%%" />' % resultado
	# 	elif self.iva.porcentaje == 0:
	# 		return '<img src="http://placehold.it/80x40/069F9C/FFFFFF/&text=$+%.2f" title= "Sin Iva" />' % resultado
	# 	else:
	# 		return '<img src="http://placehold.it/80x40/B3888F/FFFFFF/&text=$+%.2f" title= "%.1f%%" />' % (resultado, self.iva.porcentaje)



class Factura_emitida(Factura):
	ente = models.ForeignKey(Empresa_Ente)

	def __unicode__(self):
		return "para: " + unicode(self.ente) + " - fecha: "+unicode(self.fecha)


class Informes(models.Model):
    class Meta:
        permissions = (("can_view_informe", "Can view informe"),)


class Albaran(models.Model):
	registrado_el = models.DateField(default=datetime.datetime.now, 
		help_text="Cambie este campo sólo en caso de registrar una albaran para un mes anterior, tenga en cuenta que al registrar para otro mes éste no se incluirá en los informes del mes actual.")
	fecha = models.DateField()
	nro_albaran = models.CharField(max_length=15, blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2)

	
	class Meta:
		abstract = True



class Albaran_emitido(Albaran):
	ente = models.ForeignKey(Empresa_Ente)

	def __unicode__(self):
		return "para: " + unicode(self.ente) + " - fecha: "+unicode(self.fecha)


class Albaran_recibido(Albaran):
	emisor = models.ForeignKey(Empresa_Ente)

	def __unicode__(self):
		return "de: " + unicode(self.emisor) + " - fecha: "+unicode(self.fecha)


