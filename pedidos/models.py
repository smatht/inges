# encoding:utf-8
import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html

from facturacion.models import Proveedor, Registro
from proyectos.models import Obra


class ExtendUser(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  dni = models.IntegerField(blank=True, null=True)


class PedidoCabecera(models.Model):
  # cuit = lambda: Registro.objects.get(cuit='23144591119')
  registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
  fecha = models.DateField(default=datetime.datetime.now)
  proveedor = models.ForeignKey(Proveedor)
  se_autoriza = models.ForeignKey(User, related_name='toUser', verbose_name='Se autoriza a', blank=True, null=True)
  destino = models.ForeignKey(Obra, verbose_name='Obra')
  remitente = models.ForeignKey(User, related_name='fromUser', help_text='Persona que autoriza')

  class Meta:
    verbose_name = 'Pedido'
    verbose_name_plural = 'Pedidos'

  def account_actions(self):
    return format_html(
      '<a class="button" href="{}" target="_blank">Imprimir</a>',
      reverse('admin:account-deposit', args=[self.pk]),
    )
  account_actions.short_description = 'Acciones'
  account_actions.allow_tags = True


class PedidoDetalle(models.Model):
  orden_retiro = models.ForeignKey(PedidoCabecera)
  descripcion = models.CharField(max_length=140)
  cantidad = models.CharField(max_length=10)
  UNIDAD_MEDIDA = (
    ('un', 'unidades'),
    ('mt', 'metros'),
    ('m2', 'metros cuadrados'),
    ('m3', 'metros cubicos'),
    ('gr', 'gramos'),
    ('kg', 'kilogramos'),
    ('lt', 'litros'),
    ('ml', 'milimetros'),
    ('km', 'kilómetros'),
    ('tn', 'toneladas'),
    ('om', 'otras medidas'),
  )
  medida = models.CharField(
    max_length=2,
    choices=UNIDAD_MEDIDA,
    default='un',
  )

class RemitoCabecera(models.Model):
  # cuit = lambda: Registro.objects.get(cuit='23144591119')
  pedido = models.ForeignKey(PedidoCabecera, blank=True, null=True)
  numeroRemito = models.CharField(max_length=20)
  fecha = models.DateField(default=datetime.datetime.now)
  destino = models.CharField(max_length=30)


class RemitoDetalle(models.Model):
  remito = models.ForeignKey(RemitoCabecera)
  descripcion = models.CharField(max_length=140)
  cantidad = models.CharField(max_length=10)
  UNIDAD_MEDIDA = (
    ('un', 'unidades'),
    ('mt', 'metros'),
    ('m2', 'metros cuadrados'),
    ('m3', 'metros cubicos'),
    ('gr', 'gramos'),
    ('kg', 'kilogramos'),
    ('lt', 'litros'),
    ('ml', 'milimetros'),
    ('km', 'kilómetros'),
    ('tn', 'toneladas'),
    ('om', 'otras medidas'),
  )
  medida = models.CharField(
    max_length=2,
    choices=UNIDAD_MEDIDA,
    default='un',
  )
  importe = models.DecimalField(max_digits=10, decimal_places=2)