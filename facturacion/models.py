from django.db import models
#from django.contrib.auth.models import User


class Iva(models.Model):
	porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

	def __unicode__(self):
		return unicode(self.porcentaje)


class Empresa(models.Model):
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return unicode(self.nombre)


class Factura_recibida(models.Model):
	fecha = models.DateField()
	emisor = models.ForeignKey(to=Empresa, related_name="pertenece")
	nro_factura = models.CharField(max_length=15)
	neto = models.DecimalField(max_digits=6, decimal_places=2)
	iva = models.ForeignKey(to=Iva, related_name="posee")
	percepciones_otros = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	# Para registrar al usuario que agrega el registro
	# usuario = models.ForeignKey(User)

	# Para saberla fecha y hora de ingreso del registro
	# timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		# Optimo
		# return "%s - %s" (self.emisor, self.nro_factura)
		
		return unicode(self.emisor)+" - "+self.nro_factura

	def valor_iva_imagen(self):
		resultado = (self.iva.porcentaje * self.neto)/100
		if self.iva.porcentaje == 21:
			return 'http://placehold.it/80x4 0/89B51F/ffffff/&text=$+%.2f' % resultado
		elif self.iva.porcentaje == 10.5:
			return 'http://placehold.it/80x4 0/E8117F/ffffff/&text=$+%.2f' % resultado

	def impuesto(self):
		resultado = (self.iva.porcentaje * self.neto)/100
		return resultado

	def total(self):
		resultado = self.neto + self.impuesto() + self.percepciones_otros
		return resultado



class Ente(models.Model):
	nombre = models.CharField(max_length=75)

	def __unicode__(self):
		return unicode(self.nombre)



class Factura_emitida(models.Model):
	fecha = models.DateField()
	ente = models.ForeignKey(to=Ente, related_name="pertenece")
	nro_factura = models.CharField(max_length=15)
	neto_iva = models.DecimalField(max_digits=6, decimal_places=2)
	# iva = models.ForeignKey(to=Iva, related_name="corresponde")

	def iva(self):
		resultado = self.neto_iva - (self.neto_iva/1.21)
		return resultado

	
