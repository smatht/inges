from django.db import models
#from django.contrib.auth.models import User


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

	def __unicode__(self):
		return unicode(self.nombre)

class Localidad(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return unicode(self.nombre)


class Empresa(models.Model):
	nombre = models.CharField(max_length=75)
	direccion = models.CharField(max_length=140, blank=True)
	telefono = models.CharField(max_length=50, blank=True)
	telefono_secundario = models.CharField(max_length=50, blank=True)
	pais = models.ForeignKey(to=Pais, related_name="radicada", blank=True, null=True)
	ciudad = models.ForeignKey(to=Ciudad, related_name="pertenece", blank=True, null=True)
	localidad = models.ForeignKey(to=Localidad, related_name="pertenece", blank=True, null=True)

	def __unicode__(self):
		return unicode(self.nombre)


class Factura_recibida(models.Model):
	fecha = models.DateField()
	registrado_el = models.DateTimeField(auto_now_add = True)
	emisor = models.ForeignKey(to=Empresa, related_name="pertenece")
	nro_factura = models.CharField(max_length=15, blank=True)
	neto = models.DecimalField(max_digits=10, decimal_places=2)
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
	registrado_el = models.DateTimeField(auto_now_add = True)
	ente = models.ForeignKey(to=Ente, related_name="pertenece")
	nro_factura = models.CharField(max_length=15)
	neto_iva = models.DecimalField(max_digits=10, decimal_places=2)
	# iva = models.ForeignKey(to=Iva, related_name="corresponde")

	def __unicode__(self):
		
		return "para: " + unicode(self.ente) + " - fecha: "+unicode(self.fecha)

	def iva(self):
		resultado = float(self.neto_iva) - (float(self.neto_iva)/float(1.21))
		return resultado


class Informes(models.Model):
    class Meta:
        permissions = (("can_view_informe", "Can view informe"),)



