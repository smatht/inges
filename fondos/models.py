# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.db import models
from mantenimiento.models import TiposDoc
from facturacion.models import Registro
from proyectos.models import Obra
from facturacion.models import Proveedor
from compras.models import Compra
from fondos_externos.models import Cuenta


class TipoCaja(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'

    def __unicode__(self):
        return format(self.descripcion)


class Caja(models.Model):
    tipoCaja = models.ForeignKey(TipoCaja, on_delete=models.CASCADE)
    fApertura = models.DateTimeField(default=datetime.datetime.now)
    fCierre = models.DateTimeField(null=True, blank=True)
    montoInicial = models.FloatField(default=0)
    acumEntradas = models.FloatField(default=0)
    acumSalidas = models.FloatField(default=0)
    destino = models.ForeignKey(Obra, on_delete=models.CASCADE)
    cuentaWallet = models.ForeignKey(Cuenta, verbose_name='Cuenta Wallet', null=True, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return format(self.tipoCaja.__unicode__() + ' Obra: ' + self.destino.__unicode__()
                      + ' ' + self.fApertura.strftime("%d-%m-%Y"))


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
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Registro, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora')
    tipoDoc = models.ForeignKey(TiposDoc, null=True, blank=True, verbose_name='Tipo de documento', on_delete=models.CASCADE)
    numDoc = models.IntegerField(null=True, blank=True, verbose_name='Numero de documento')
    descripcion = models.CharField(max_length=100)
    operador = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    importe = models.FloatField()
    tipoMovCaja = models.ForeignKey(TipoMovCaja, verbose_name='Operacion', on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Movimiento de caja'
        verbose_name_plural = 'Movimientos de caja'


class OrdenPago(models.Model):
    empresa = models.ForeignKey(Registro, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fPago = models.DateField(default=datetime.datetime.now, verbose_name='Fecha pago')
    fCarga = models.DateTimeField(default=datetime.datetime.now) #No admin
    importe = models.FloatField()
    operador = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    anulado = models.BooleanField(default=False)
    aplicado = models.BooleanField(default=False)
    comentario = models.CharField(max_length=100, null=True, blank=True)
    facturas = models.ManyToManyField(Compra, blank=True)
    # Si es pago en efectivo
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if self.diferencia != 0:
    #         return  # No se graba!
    #     else:
    #         super(OrdenPago, self).save(*args, **kwargs)
