# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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
    tipoCaja = models.ForeignKey(TipoCaja)
    fApertura = models.DateTimeField(default=datetime.datetime.now)
    fCierre = models.DateTimeField(null=True, blank=True)
    montoInicial = models.FloatField(default=0)
    acumEntradas = models.FloatField(default=0)
    acumSalidas = models.FloatField(default=0)
    destino = models.ForeignKey(Obra)
    idCuentaWallet = models.CharField(max_length=40, null=True, blank=True)
    nombreCuentaWallet = models.CharField(max_length=50, null=True, blank=True)

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
    caja = models.ForeignKey(Caja)
    empresa = models.ForeignKey(Registro)
    fecha = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora')
    tipoDoc = models.ForeignKey(TiposDoc, null=True, blank=True, verbose_name='Tipo de documento')
    numDoc = models.IntegerField(null=True, blank=True, verbose_name='Numero de documento')
    descripcion = models.CharField(max_length=100)
    operador = models.ForeignKey(User, null=True)
    importe = models.FloatField()
    tipoMovCaja = models.ForeignKey(TipoMovCaja, verbose_name='Operacion')
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    origen = models.SmallIntegerField(default=0)
    idWallet = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = 'Movimiento de caja'
        verbose_name_plural = 'Movimientos de caja'

    def save(self, *args, **kwargs):
        # TODO: Que la actualizacion de caja sea con los valores actuales de la caja no con los valores de caja del objeto.
        # TODO: Puede darse el caso de que la secuencia de gravacion no sea la esperada
        try:
            objYaExistente = MovCaja.objects.get(pk=self.pk)
            objDuplicado = MovCaja.objects.get(idWallet=self.idWallet)
            print('Existente: ' + str(objYaExistente.pk))
            print('Duplicado: ' + str(objDuplicado.idWallet))
        except ObjectDoesNotExist:
            print('ObjectDoesNot Exist')
            objYaExistente = None
            objDuplicado = None
        if objDuplicado == None:
            if objYaExistente != None:
                self.importe = 0

            if getattr(self, 'fecha', None) is None:
                self.fecha = datetime.datetime.now
            if getattr(self, 'tipoMovCaja').suma:
                self.caja.acumEntradas += self.importe
            else:
                self.caja.acumSalidas += self.importe
            self.caja.save()
            super(MovCaja, self).save(*args, **kwargs)
        else:
            return


class OrdenPago(models.Model):
    empresa = models.ForeignKey(Registro)
    proveedor = models.ForeignKey(Proveedor)
    fPago = models.DateField(default=datetime.datetime.now, verbose_name='Fecha pago')
    fCarga = models.DateTimeField(default=datetime.datetime.now) #No admin
    importe = models.FloatField()
    operador = models.ForeignKey(User, null=True)
    anulado = models.BooleanField(default=False)
    aplicado = models.BooleanField(default=False)
    comentario = models.CharField(max_length=100, null=True, blank=True)
    facturas = models.ManyToManyField(Compra, blank=True)
    # Si es pago en efectivo
    caja = models.ForeignKey(Caja)

    # def save(self, *args, **kwargs):
    #     print(self.diferencia)
    #     if self.diferencia != 0:
    #         return  # No se graba!
    #     else:
    #
        # super(OrdenPago, self).save(*args, **kwargs)
