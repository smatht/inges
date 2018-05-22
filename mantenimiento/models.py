# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from facturacion.models import Registro
from fondos.models import TipoCaja
from proyectos.models import Obra


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(blank=True, null=True)
    habilitarPedido = models.BooleanField(default=False, verbose_name='Habilitar orden de retiro',
                                          help_text='(Marque este campo en caso de que el usuario pueda generar '
                                                    'una orden de retiro con su firma)')

# Create your models here.

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
##########  D E P R E C A T E D #######################################################################################
#######################################################################################################################
#######################################################################################################################
'''
  22/05/2018 Este modelo fue a parar al modulo "COMUN" por problemas de referencias cruzadas.
  Eliminar solo cuando se hayan hecho las migraciones de tablas para no perder datos.
'''
class TiposDoc(models.Model):
    id = models.CharField(max_length=3, primary_key=True, verbose_name='Nombre')
    descripcion = models.CharField(max_length=50)
    esFactura = models.BooleanField(default=False)
    STOCK = (
        (1, 'Aumenta'),
        (-1, 'Disminuye'),
        (0, 'No aplica'),
    )
    TIPO = (
        (0, 'Factura de venta'),
        (1, 'Factura de compra'),
        (2, 'Presupuesto'),
        (3, 'Otro documento'),
    )
    aplicaStock = models.SmallIntegerField(choices=STOCK, verbose_name='Cambia stock')
    tipo = models.SmallIntegerField(choices=TIPO)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        db_table = 'TiposDoc'
#######################################################################################################################
#######################################################################################################################
#############  D E P R E C A T E D  ###################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
##########  D E P R E C A T E D #######################################################################################
#######################################################################################################################
#######################################################################################################################
'''
  22/05/2018 Este modelo fue a parar al modulo "COMUN" por problemas de referencias cruzadas.
  Eliminar solo cuando se hayan hecho las migraciones de tablas para no perder datos.
'''
class TipoImpuesto(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'TiposImpuesto'
#######################################################################################################################
#######################################################################################################################
#############  D E P R E C A T E D  ###################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
##########  D E P R E C A T E D #######################################################################################
#######################################################################################################################
#######################################################################################################################
'''
  22/05/2018 Este modelo fue a parar al modulo "COMUN" por problemas de referencias cruzadas.
  Eliminar solo cuando se hayan hecho las migraciones de tablas para no perder datos.
'''
class Impuesto(models.Model):
    descripcion = models.CharField(max_length=50)
    TIPO = (
        (0, 'Impuesto interno'),
        (1, 'IVA'),
        (2, 'DGR'),
        (3, 'Otro'),
    )
    tipoImpuesto = models.SmallIntegerField(choices=TIPO)
    valorImpuesto = models.FloatField()
    esPorcentaje = models.BooleanField(default=True)
    esObligatorio = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        db_table = 'Impuestos'
#######################################################################################################################
#######################################################################################################################
#############  D E P R E C A T E D  ###################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
##########  D E P R E C A T E D #######################################################################################
#######################################################################################################################
#######################################################################################################################
'''
  22/05/2018 Este modelo fue a parar al modulo "COMUN" por problemas de referencias cruzadas.
  Eliminar solo cuando se hayan hecho las migraciones de tablas para no perder datos.
'''
class TipoMovCaja(models.Model):
    descripcion = models.CharField(max_length=75)
    suma = models.BooleanField(default=False)

    class Meta:
        db_table = 'TiposMovCaja'
        ordering = ['pk']
        verbose_name = 'Tipo movimiento'
        verbose_name_plural = 'Tipo movimiento'

    def __unicode__(self):
        return format(self.descripcion)
#######################################################################################################################
#######################################################################################################################
#############  D E P R E C A T E D  ###################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


class Configuracion(models.Model):
    compras_condPago = models.CharField(
        max_length=3,
        choices=settings.COND_PAGO,
        default='CTD',
        verbose_name='Condición pago',
    )
    empresa = models.ForeignKey(
        Registro,
        null=True,
        blank=True,
        verbose_name='Empresa principal')
    compras_tipoDoc = models.ForeignKey(
        TiposDoc,
        related_name='tipoFacCompra',
        null=True,
        blank=True,
        verbose_name='Tipo doc')
    compras_usaPrFinal = models.BooleanField()
    compras_FacAfectaStk = models.BooleanField()
    compras_tipoMovCajaDef = models.ForeignKey(
        TipoMovCaja,
        related_name='tipoMovCajaCompra',
        null=True,
        blank=True,
        verbose_name='Tipo Mov Caja por defecto')
    ventas_tipoDoc = models.ForeignKey(
        TiposDoc,
        related_name='tipoFacVenta',
        null=True,
        blank=True,
        verbose_name='Tipo doc')
    fondos_orden_pago_movimiento = models.ForeignKey(
        TipoMovCaja,
        related_name='tipoMovCaja',
        null=True,
        blank=True,
        verbose_name='Tipo movimiento de caja')
    general_tipoCaja = models.ForeignKey(
        TipoCaja,
        related_name='tipoCaja',
        null=True,
        blank=True,
        verbose_name='Tipo de caja')
    general_obraCaja = models.ForeignKey(
        Obra,
        related_name='obraCaja',
        null=True,
        blank=True,
        verbose_name='Obra de caja')

    def __unicode__(self):
        return unicode('Ajustes')

    class Meta:
        db_table = 'Configuraciones'