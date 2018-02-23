# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from facturacion.models import Registro


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(blank=True, null=True)
    habilitarPedido = models.BooleanField(default=False, verbose_name='Habilitar orden de retiro',
                                          help_text='(Marque este campo en caso de que el usuario pueda generar '
                                                    'una orden de retiro con su firma)')

# Create your models here.


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


class TipoImpuesto(models.Model):
    descripcion = models.CharField(max_length=50)


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
    ventas_tipoDoc = models.ForeignKey(
        TiposDoc,
        related_name='tipoFacVenta',
        null=True,
        blank=True,
        verbose_name='Tipo doc')

    def __unicode__(self):
        return unicode('Ajustes')