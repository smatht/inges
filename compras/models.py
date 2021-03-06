# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html

from facturacion.models import Registro, Registro_factura, Proveedor
from proyectos.models import Obra

from stock.models import Producto, Unidades
from common.models import TiposDoc, Impuesto


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
        db_table = 'Pedidos'
        ordering = ['-fechaPedido']
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Ordenes de compra'

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
        db_table = 'PedidosItems'
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
        db_table = 'PedidosItemsConceptos'
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
        db_table = 'Remitos'
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
        db_table = 'RemitosItems'
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
    numDoc = models.IntegerField(verbose_name='Número')
    fDocumento = models.DateField(verbose_name='Fecha del documento')
    fRegistro = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de carga')
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
        verbose_name='Condicion pago',
    )
    esCopia = models.BooleanField(default=False, verbose_name='Es copia')
    afectaStock = models.BooleanField(default=True, verbose_name='Afecta a stock')
    yaAfectoStock = models.BooleanField(default=False)
    prFinal = models.BooleanField(default=True, verbose_name='Utiliza precio final')
    fContabilizar = models.DateField(default=datetime.datetime.now, verbose_name='Fecha contable', help_text='Afecta a informes '                                                                                        'contables.')
    cai = models.BigIntegerField(null=True, blank=True)
    vCai = models.DateField(null=True, blank=True)
    fVencimiento = models.DateField(verbose_name='Fecha de vencimiento', default=datetime.datetime.now)
    idCaja = models.IntegerField(blank=True, null=True)
    afectaCaja = models.BooleanField(default=True, verbose_name='Generar mov. caja')
    fSaldada = models.DateTimeField(null=True, blank=True)

    def saldo(self):
        if self.condPago == 'CRE':
            try:
                return DocCuentaProveedor.objects.get(documento=self).importeSaldo
            except ObjectDoesNotExist:
                return self.totNeto
        else:
            return self.totNeto

    def NumeroIdentificacion(self):
        return self.sucursal.__str__().zfill(4) + " - " + self.numDoc.__str__().zfill(8)

    class Meta:
        db_table = 'Compras'
        verbose_name_plural = "Compras"
        unique_together = (('tipoDoc', 'sucursal', 'numDoc', 'proveedor'),)

    def __unicode__(self):
        return self.tipoDoc.id + " " + self.sucursal.__str__().zfill(4) + " - " + self.numDoc.__str__().zfill(8) \
               + " Saldo: " + unicode(self.saldo()) + " Vto: " + unicode(self.fVencimiento) \
               + " (" + unicode(self.proveedor) + ": " + unicode(self.obra) + ")"



class CompraItem(models.Model):
    factura = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    cantidad = models.FloatField()
    alicuota = models.ForeignKey(Impuesto)
    precio_unitario = models.FloatField()
    # obra = models.ForeignKey(Obra, blank=True, null=True)

    class Meta:
        db_table = 'ComprasItems'
        verbose_name = 'Detalle de documento'
        verbose_name_plural = 'Detalle de documento'


class CompraItemConcepto(models.Model):
    factura = models.ForeignKey(Compra)
    descripcion = models.CharField(max_length=300)
    cantidad = models.FloatField()
    alicuota = models.ForeignKey(Impuesto)
    precio_unitario = models.FloatField()
    # obra = models.ForeignKey(Obra, blank=True, null=True)

    class Meta:
        db_table = 'ComprasItemsConceptos'
        verbose_name = 'Concepto'
        verbose_name_plural = 'Conceptos'


class ImpuestoXCompra(models.Model):
    factura = models.ForeignKey(Compra)
    impuesto = models.ForeignKey(Impuesto)
    importe_neto = models.FloatField()

    class Meta:
        db_table = 'ImpuestoXCompra'
        verbose_name = 'Otro impuesto'
        verbose_name_plural = 'Otros impuestos'


class DocCuentaProveedor(models.Model):
    documento = models.ForeignKey(Compra)
    importeDocumento = models.FloatField()
    importePagado = models.FloatField(default=0)
    importeSaldo = models.FloatField()

    class Meta:
        db_table = 'DocCuentaProveedor'



