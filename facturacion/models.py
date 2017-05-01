# encoding:utf-8
from django.contrib.auth.models import User
from django.db import models
import datetime
# from django.contrib.auth.models import User
# from suit.widgets import SuitDateWidget


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


############################################
#          Clases Empresas                 #
############################################

class Empresa(models.Model):
  domicilio_fiscal = models.CharField(max_length=140, blank=True)
  telefono = models.CharField(max_length=50, blank=True)
  telefono_secundario = models.CharField(max_length=50, blank=True)
  email = models.EmailField(blank=True)
  pais = models.ForeignKey(Pais, blank=True, null=True)
  ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
  localidad = models.ForeignKey(Localidad, blank=True, null=True)

	# class Meta:
  #   ordering = ['nombre']

  def __unicode__(self):
    return unicode(self.nombre)

class Proveedor(Empresa):
  razon_social = models.CharField(max_length=75)
  domicilio_comercial = models.CharField(max_length=140, blank=True)
  cuit = models.CharField(max_length=20, blank=True)
  sitio_web = models.CharField(max_length=140, blank=True)

  class Meta:
    ordering = ['razon_social']
    verbose_name_plural = "proveedores"

  def __unicode__(self):
    return unicode(self.razon_social)


class Cliente(Empresa):
  nombre = models.CharField(max_length=75)
  dni = models.IntegerField(blank=True, null=True)
  cuil = models.CharField(max_length=20, blank=True)

  class Meta:
    ordering = ['nombre']

  def __unicode__(self):
    return unicode(self.nombre)

class Registro(Empresa):
  nombre_fantasia = models.CharField(max_length=50, blank=True, null=True)
  razon_social = models.CharField(max_length=50)
  cuit = models.CharField(max_length=20)
  domicilio_comercial = models.CharField(max_length=140)
  IVA = (
    ('RI', 'IVA RESPONSABLE INSCRIPTO'),
    ('RNI', 'IVA RESPONSABLE NO INSCRIPTO'),
    ('RM', 'IVA RESPONSABLE MONOTRIBUTO'),
    ('EX', 'IVA SUJETO EXENTO'),
    ('NR', 'IVA NO RESPONSABLE'),
  )
  iva = models.CharField(
    max_length=2,
    choices=IVA,
    default='RI',
  )
  fecha_inicio_actividad = models.DateField(blank=True, null=True)
  membrete = models.ImageField(upload_to='user_img/', blank=True, null=True)
  logo = models.ImageField(upload_to='user_img/', blank=True, null=True)

  class Meta:
    ordering = ['nombre_fantasia']
    verbose_name_plural = "Registro empresa"
    verbose_name = "Empresa"


  def __unicode__(self):
    if (self.nombre_fantasia):
      return unicode(self.nombre_fantasia)
    else:
      return unicode(self.razon_social)


# class Material(models.Model):
#   proveedor = models.ForeignKey(Proveedor)
#   descripcion = models.CharField(max_length=50)
#
#   # Unidades de medida
#   #////////////////////////////////////////////
#   UNIDADES = 'un'
#   METROS = 'mts'
#   CENTIMETROS = 'cm'
#   LITRO = 'lts'
#   KILO = 'kg'
#   METRO_CUBICO = 'm3'
#   UNIDADES_MEDIDA = (
#     (UNIDADES, 'Unidades'),
#     (METROS, 'Metros'),
#     (CENTIMETROS, 'Centimetros'),
#     (LITRO, 'Litro'),
#     (KILO, 'Kilo'),
#     (METRO_CUBICO, 'Metro Cubico'),
#   )
#   #//////////////////////////////////////////
#
#   unidad_medida = models.CharField(max_length=3, choices=UNIDADES_MEDIDA, default=UNIDADES)


############################################
#     Clases principales Facturacion       #
############################################
class Factura(models.Model):
  fecha_registro = models.DateField(default=datetime.datetime.now,
		help_text="Cambie este campo sólo en caso de registrar una factura para un mes anterior, tenga en cuenta que al registrar para otro mes ésta no se incluirá en los informes del mes actual.")
  fecha_factura = models.DateField()
  nro_factura = models.CharField(max_length=20)
  TIPO = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
  )
  tipo = models.CharField(
    max_length=1,
    choices=TIPO,
    default='a',
  )
  # percepciones_otros = models.DecimalField(max_digits=6, decimal_places=2, default=0)
  observaciones = models.TextField(blank=True)

  class Meta:
    abstract = True


class Registro_factura(Factura):
  # cuit = lambda: Registro.objects.get(cuit='23144591119')
  emisor = models.ForeignKey(Proveedor)
  registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
  pagado = models.BooleanField(default=True)
  esCopia = models.BooleanField(default=False)
  # Para registrar al usuario que agrega el registro
  usuario = models.ForeignKey(User, null=True)

  class Meta:
    verbose_name_plural = "registro facturas"
	
  def total(self):
    resultado = self.subtotal() + self.impuesto()
    return resultado


  def impuesto(self):
    resultado = 0
    detalles = Factura_detalle.objects.filter(factura=self)
    for d in detalles:
      subtotal = d.cantidad * d.precio_unitario
      resultado += (d.alicuota.porcentaje * subtotal)/100
    return resultado

  def subtotal(self):
    subtotal = 0
    detalles = Factura_detalle.objects.filter(factura=self)
    for d in detalles:
      subtotal += d.cantidad * d.precio_unitario
    return subtotal

# Para saberla fecha y hora de ingreso del registro
# timestamp = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return unicode(self.fecha_factura)+" - "+self.nro_factura

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


class Factura_detalle(models.Model):
  factura = models.ForeignKey(Registro_factura)
  descripcion = models.CharField(max_length=140)
  cantidad = models.PositiveSmallIntegerField()
  alicuota = models.ForeignKey(Iva)
  precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)


class Emision_factura(Factura):
  from proyectos.models import Obra
  cliente = models.ForeignKey(Cliente)
  obra = models.ForeignKey(Obra, blank=True, null=True)
  # Para registrar al usuario que agrega el registro
  usuario = models.ForeignKey(User, null=True)

  class Meta:
    verbose_name_plural = "emisión facturas"

  def impuesto(self):
    resultado = 0
    detalles = Emision_detalle.objects.filter(factura=self)
    for d in detalles:
      resultado += d.total - (d.total / ((d.alicuota.porcentaje / 100) + 1))
    return resultado

  def total(self):
    resultado = 0
    detalles = Emision_detalle.objects.filter(factura=self)
    for d in detalles:
      resultado += d.total
    return resultado

  def __unicode__(self):
    detalles = Emision_detalle.objects.filter(factura=self)
    if (detalles.count() > 0):
      detalleResumen = detalles.first().descripcion[:50]
    else:
      detalleResumen = ''
    return "para: " + unicode(self.cliente) + " - fecha: "+unicode(self.fecha_factura) + ' - "' +detalleResumen+ '..."'

class Emision_detalle(models.Model):
  factura = models.ForeignKey(Emision_factura)
  descripcion = models.CharField(max_length=140)
  cantidad = models.PositiveSmallIntegerField()
  alicuota = models.ForeignKey(Iva)
  total = models.DecimalField(max_digits=10, decimal_places=2)


class Informes(models.Model):
  class Meta:
    permissions = (("can_view_informe", "Can view informe"),)


class Recibo(models.Model):
  emisor = models.ForeignKey(Proveedor)
  fecha_registro = models.DateField(default=datetime.datetime.now,
		help_text="Cambie este campo sólo en caso de registrar una albaran para un mes anterior, tenga en cuenta que al registrar para otro mes éste no se incluirá en los informes del mes actual.")
  fecha_recibo = models.DateField()
  nro_recibo = models.CharField(max_length=15, blank=True)
  detalle = models.TextField(blank=True)
  total = models.DecimalField(max_digits=10, decimal_places=2)