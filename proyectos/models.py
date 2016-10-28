from django.db import models

from facturacion.models import Pais, Ciudad, Localidad, Cliente


class Obra(models.Model):
  descripcion = models.CharField(max_length=140, blank=False, null=False)
  descripcion_corta = models.CharField(max_length=30, blank=True, null=True)
  fecha_inicio = models.DateField(auto_now=False, auto_now_add=False)
  fecha_fin = models.DateField(auto_now=False, auto_now_add=False)
  pais = models.ForeignKey(Pais, blank=True, null=True)
  ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
  localidad = models.ForeignKey(Localidad, blank=True, null=True)
  cliente = models.ForeignKey(Cliente, blank=False, null=False)