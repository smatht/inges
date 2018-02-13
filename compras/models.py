# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html

from facturacion.models import Registro, Registro_factura, Proveedor
from proyectos.models import Obra

from stock.models import Producto, Unidades

from mantenimiento.models import TiposDoc, Impuesto


class Pedido(models.Model):
    usuario = models.ForeignKey(User, null=True)
    # cuit = lambda: Registro.objects.get(cuit='23144591119')
    registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    fechaPedido = models.DateField(default=datetime.datetime.now, verbose_name='Fecha')
    fechaCarga = models.DateTimeField(default=datetime.datetime.now)
    proveedor = models.ForeignKey(Proveedor)
    se_autoriza = models.ForeignKey(User, related_name='toUser1', verbose_name='Se autoriza a', blank=True, null=True)
    destino = models.ForeignKey(Obra, verbose_name='Obra')
    bGeneraRemito = models.BooleanField(default=False, verbose_name="Recepción inmediata")
    firmante = models.ForeignKey(User, related_name='fromUser1', help_text='Persona que autoriza', blank=True, null=True)
    remitente = models.ForeignKey(User, related_name='registerUser1', help_text='Persona que registra')
    bAnulado = models.BooleanField(default=False)

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
    producto = models.ForeignKey(Producto)
    sAclaracion = models.CharField(max_length=150, null=True, blank=True, verbose_name='aclaracion')
    sCantidad = models.CharField(max_length=10, verbose_name='cantidad', default='1')
    unidades = models.ForeignKey(Unidades, default=1)
    # precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return unicode(self.producto.descripcion + ' [' + str(self.sCantidad) + ']')


class PedidoItemConcepto(models.Model):
    pedido = models.ForeignKey(Pedido)
    sDescripcion = models.CharField(max_length=300, verbose_name='descripcion')
    sCantidad = models.CharField(max_length=10, verbose_name='cantidad', default='1')
    unidades = models.ForeignKey(Unidades, default=1)
    # precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'


class Remito(models.Model):
    usuario = models.ForeignKey(User, null=True)
    # cuit = lambda: Registro.objects.get(cuit='23144591119')
    factura = models.ForeignKey(Registro_factura, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, blank=True, null=True)
    registro = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    proveedor = models.ForeignKey(Proveedor, blank=True, null=True)
    sNumeroRemito = models.CharField(max_length=20, blank=True, null=True, verbose_name='Numero remito')
    fechaRemito = models.DateField(default=datetime.datetime.now)
    fechaCarga = models.DateTimeField(default=datetime.datetime.now)
    destino = models.ForeignKey(Obra, blank=True, null=True)
    sObservaciones = models.TextField(blank=True)
    iOrigen = models.SmallIntegerField(default=0)
    # (origen) Se usa para saber si el remito se creo a partir de un pedido o no
    # afectaStock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Remito'
        verbose_name_plural = 'Remitos'

    def __unicode__(self):
        return unicode(self.fechaRemito.strftime('%d/%m/%Y') + ' - ' + str(self.proveedor) + ' - ' + str(self.destino))


class RemitoItem(models.Model):
    remito = models.ForeignKey(Remito)
    bConfirmacion = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto)
    sCantidad = models.CharField(max_length=10)
    unidades = models.ForeignKey(Unidades, default=1)
    # precioUnitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # importe = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __unicode__(self):
        return unicode(self.producto.descripcion + ' [' + str(self.sCantidad) + ']')

#######################################################################################
#### IMPLEMENTAR REMITO ITEM CONCEPTO
#######################################################################################


############################################
#  Clases principal Facturacion Compras    #
############################################
class AbstractCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor)
    tipoDoc = models.ForeignKey(TiposDoc, verbose_name='Documento')
    sucursal = models.IntegerField()
    numDoc = models.IntegerField(verbose_name='Numero')
    fDocumento = models.DateField(verbose_name='Fecha del documento')
    fRegistro = models.DateTimeField(default=datetime.datetime.now)
    operador = models.ForeignKey(User, null=True)
    observaciones = models.TextField(null=True, blank=True)
    anulado = models.BooleanField(default=False)
    fanulacion = models.DateTimeField(null=True, blank=True)
    afectaEmpresa = models.ForeignKey(Registro, default=1, verbose_name='Empresa')
    obra = models.ForeignKey(Obra)

    class Meta:
        abstract = True
        # unique_together = (('proveedor', 'tipoDoc', 'sucursal', 'numDoc'),)


class Compra(AbstractCompra):
    totBruto = models.FloatField(null=True, blank=True)
    totImpuestos = models.FloatField(null=True, blank=True)
    totDescuentos = models.FloatField(null=True, blank=True)
    totNeto = models.FloatField(null=True, blank=True)
    condPago = models.CharField(
        max_length=3,
        choices=settings.COND_PAGO,
        default='CTD',
        verbose_name='Condición pago',
    )
    esCopia = models.BooleanField(default=False, verbose_name='Es copia')
    afectaStock = models.BooleanField(default=False, verbose_name='Afecta a stock')
    yaAfectoStock = models.BooleanField(default=False)
    prFinal = models.BooleanField(default=True, verbose_name='Utiliza precio final')
    fContabilizar = models.DateField(default=datetime.datetime.now, verbose_name='Fecha contable', help_text='Afecta a informes '
                                                                                                     'contables.')
    cai = models.BigIntegerField(null=True, blank=True)
    vCai = models.DateField(null=True, blank=True)
    fVencimiento = models.DateField(verbose_name='Fecha de vencimiento')

    class Meta:
        verbose_name_plural = "registro facturas"

    def __unicode__(self):
        return unicode(self.fDocumento) + " - " + self.numDoc.__str__()

class CompraItem(models.Model):
    factura = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    cantidad = models.FloatField()
    alicuota = models.ForeignKey(Impuesto)
    precio_unitario = models.FloatField()
    obra = models.ForeignKey(Obra, blank=True, null=True)

    class Meta:
        verbose_name = 'Detalle de factura'
        verbose_name_plural = 'Detalle de factura'


class CompraItemConcepto(models.Model):
    factura = models.ForeignKey(Compra)
    descripcion = models.CharField(max_length=300)
    cantidad = models.FloatField()
    alicuota = models.ForeignKey(Impuesto)
    precio_unitario = models.FloatField()
    obra = models.ForeignKey(Obra, blank=True, null=True)

    class Meta:
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'
