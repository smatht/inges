from django.db import models

from facturacion.models import Pais, Ciudad, Localidad, Cliente


class Obra(models.Model):
  descripcion = models.TextField(max_length=300, verbose_name='Obra', blank=False, null=False)
  descripcion_corta = models.CharField(max_length=30, blank=True, null=True)
  fecha_inicio = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
  fecha_fin = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
  pais = models.ForeignKey(Pais, blank=True, null=True, on_delete=models.CASCADE)
  ciudad = models.ForeignKey(Ciudad, blank=True, null=True, on_delete=models.CASCADE)
  localidad = models.ForeignKey(Localidad, blank=True, null=True, on_delete=models.CASCADE)
  cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.CASCADE)

  # def __unicode__(self):
  #   return unicode(self.descripcion)

  def __unicode__(self):
    if (self.descripcion_corta):
      return unicode(self.descripcion_corta)
    else:
      return unicode(self.descripcion)