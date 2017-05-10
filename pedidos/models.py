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
  se_autoriza = models.ForeignKey(User, related_name='toUser', verbose_name='Se autoriza a')
  destino = models.ForeignKey(Obra, blank=True, null=True)
  remitente = models.ForeignKey(User, related_name='fromUser', help_text='Persona que autoriza')

  class Meta:
    verbose_name = 'Pedido'
    verbose_name_plural = 'Pedidos'

  def account_actions(self):
    return format_html(
      '<a class="button" href="{}" target="_blank">Imprimir</a>',
      reverse('admin:account-deposit', args=[self.pk]),
    )
  account_actions.short_description = 'Account Actions'
  account_actions.allow_tags = True


class PedidoDetalle(models.Model):
  orden_retiro = models.ForeignKey(PedidoCabecera)
  cantidad = models.CharField(max_length=10)
  descripcion = models.CharField(max_length=140)