# encoding:utf-8
import datetime

from django.contrib.auth.models import User
from django.db import models

from facturacion.models import Proveedor, Material
from proyectos.models import Obra


class OrdenRetiro_cabecera(models.Model):
  fecha = models.DateField(default=datetime.datetime.now)
  destino = models.ForeignKey(Proveedor)
  se_autoriza = models.ForeignKey(User, related_name='toUser')
  obra = models.ForeignKey(Obra)
  remitente = models.ForeignKey(User, related_name='fromUser')


class OrdenRetiro_detalle(models.Model):
  orden_retiro = models.ForeignKey(OrdenRetiro_cabecera)
  cantidad = models.DecimalField(max_digits=4, decimal_places=2)
  descripcion = models.ForeignKey(Material)