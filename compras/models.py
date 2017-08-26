# -*- coding: utf-8 -*-
import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html

from facturacion.models import Registro, Registro_factura
from facturacion.models import Proveedor
from proyectos.models import Obra


class Pedido(models.Model):
    usuario = models.ForeignKey(User, null=True)
    # cuit = lambda: Registro.objects.get(cuit='23144591119')
    registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    fechaPedido = models.DateField(default=datetime.datetime.now)
    fechaCarga = models.DateTimeField(default=datetime.datetime.now)
    proveedor = models.ForeignKey(Proveedor)
    se_autoriza = models.ForeignKey(User, related_name='toUser1', verbose_name='Se autoriza a', blank=True, null=True)
    destino = models.ForeignKey(Obra, verbose_name='Obra')
    generaRemito = models.BooleanField(default=False, verbose_name="Recepción inmediata")
    firmante = models.ForeignKey(User, related_name='fromUser1', help_text='Persona que autoriza', blank=True, null=True)
    remitente = models.ForeignKey(User, related_name='registerUser1', help_text='Persona que registra')
    anulado = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fechaPedido']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __unicode__(self):
        return unicode('[' + str(self.pk) + '] ' + self.fechaPedido.strftime('%d/%m/%Y') + ' - ' + str(self.proveedor) +
                       ' (' + str(self.destino) + ')')
        # return unicode(self.fecha.strftime('%d/%m/%Y'))


    # Botones de acciones para pedidos
    def account_actions(self):
        return format_html(
            '<a class="btn" href="{}" target="_blank" title="Mostrar pdf"><i class="icon-print"></i></a>'
            '<a class="btn" id="add_id_remito" href="{}" title="Recibir" onclick="return showRelatedObjectPopup(this, 1100, 500);"><i class="icon-check"></i></a>',
            reverse('admin:process-print', args=[self.pk]),
            reverse('admin:process-remito', args=[self.pk]),
        )

    account_actions.short_description = 'Acciones'
    account_actions.allow_tags = True


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido)
    descripcion = models.CharField(max_length=300)
    cantidad = models.CharField(max_length=10)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalle de pedido'

    def __unicode__(self):
        return unicode(self.descripcion + ' [' + str(self.cantidad) + ']')


class Remito(models.Model):
    usuario = models.ForeignKey(User, null=True)
    # cuit = lambda: Registro.objects.get(cuit='23144591119')
    factura = models.ForeignKey(Registro_factura, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, blank=True, null=True)
    registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True)
    numeroRemito = models.CharField(max_length=20, blank=True, null=True, verbose_name='Numero remito')
    fechaRemito = models.DateField(default=datetime.datetime.now)
    fechaCarga = models.DateTimeField(default=datetime.datetime.now)
    destino = models.ForeignKey(Obra, blank=True, null=True)
    observaciones = models.TextField(blank=True)
    origen = models.SmallIntegerField(default=0)
    # (origen) Se usa para saber si el remito se creo a partir de un pedido o no
    afectaStock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Remito'
        verbose_name_plural = 'Remitos'

    def __unicode__(self):
        return unicode(self.fechaRemito.strftime('%d/%m/%Y') + ' - ' + str(self.proveedor) + ' - ' + str(self.destino))


class RemitoItem(models.Model):
    remito = models.ForeignKey(Remito)
    confirmacion = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=300)
    cantidad = models.CharField(max_length=10)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Detalle de remito'
        verbose_name_plural = 'Detalle de remito'

    def __unicode__(self):
        return unicode(self.descripcion + ' [' + str(self.cantidad) + ']')
