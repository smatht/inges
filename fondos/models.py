# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models

from mantenimiento.models import TiposDoc

from facturacion.models import Registro

from proyectos.models import Obra

from facturacion.models import Proveedor


class TipoCaja(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

    def __unicode__(self):
        return format(self.descripcion)


class Caja(models.Model):
    tipoCaja = models.ForeignKey(TipoCaja)
    fApertura = models.DateTimeField(default=datetime.datetime.now)
    fCierre = models.DateTimeField(null=True, blank=True)
    montoInicial = models.FloatField(default=0)
    acumEntradas = models.FloatField(null=True, blank=True)
    acumSalidas = models.FloatField(null=True, blank=True)
    destino = models.ForeignKey(Obra)


class TipoMovCaja(models.Model):
    descripcion = models.CharField(max_length=75)
    suma = models.BooleanField(default=False)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Tipo movimiento'
        verbose_name_plural = 'Tipo movimiento'

    def __unicode__(self):
        return format(self.descripcion)


class MovCaja(models.Model):
    caja = models.ForeignKey(Caja)
    empresa = models.ForeignKey(Registro)
    fecha = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora')
    tipoDoc = models.ForeignKey(TiposDoc, null=True, blank=True)
    numDoc = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=100)
    operador = models.ForeignKey(User, null=True)
    importe = models.FloatField()
    tipoMovCaja = models.ForeignKey(TipoMovCaja, verbose_name='Operacion')
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)

    class Meta:
        verbose_name = 'Movimiento de caja'
        verbose_name_plural = 'Movimientos de caja'


# class OrdenPago(models.Model):
