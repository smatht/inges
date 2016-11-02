# encoding:utf-8
import datetime

from django.contrib.auth.models import User
from django.db import models

from facturacion.models import Proveedor
from proyectos.models import Obra


class ExtendUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dni = models.IntegerField(blank=True, null=True)


class OrdenRetiro_cabecera(models.Model):
  fecha = models.DateField(default=datetime.datetime.now)
  proveedor = models.ForeignKey(Proveedor)
  se_autoriza = models.ForeignKey(User, related_name='toUser', verbose_name='Se autoriza a')
  destino = models.ForeignKey(Obra, blank=True, null=True)
  remitente = models.ForeignKey(User, related_name='fromUser', help_text='Persona que autoriza')


class OrdenRetiro_detalle(models.Model):
  orden_retiro = models.ForeignKey(OrdenRetiro_cabecera)
  cantidad = models.CharField(max_length=10)
  descripcion = models.CharField(max_length=140)