from django.contrib.auth.models import User
from django.db import models


# Claser que extiende al modelo de usuario de Django
class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(blank=True, null=True)
    habilitarPedido = models.BooleanField(default=False, verbose_name='Habilitar orden de retiro',
                                          help_text='(Marque este campo en caso de que el usuario pueda generar '
                                                    'una orden de retiro con su firma)')

# Create your models here.


class TiposDoc(models.Model):
	id = models.CharField(max_length=3, primary_key=True)
	descripcion = models.CharField(max_length=50)
	esFactura = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.descripcion)


class TipoImpuesto(models.Model):
	descripcion = models.CharField(max_length=50)


class Impuesto(models.Model):
	descripcion = models.CharField(max_length=50)
	tiposImpuesto = models.ForeignKey(TipoImpuesto)
	valorImpuesto = models.DecimalField(max_digits=5, decimal_places=4)
	esPorcentaje = models.BooleanField()

	def __unicode__(self):
		return unicode(self.porcentaje)