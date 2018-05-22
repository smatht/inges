# -*- coding: utf-8 -*-
import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
from facturacion.models import Registro
from proyectos.models import Obra
from facturacion.models import Proveedor
from compras.models import Compra
from common.models import TiposDoc, TipoMovCaja


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
        cajaActual = Caja.objects.get(pk=self.caja.pk)
        try:
            objYaExistente = MovCaja.objects.get(pk=self.pk)
            objDuplicado = MovCaja.objects.get(idWallet=self.idWallet)
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
                cajaActual.acumEntradas += self.importe
            else:
                cajaActual.acumSalidas += self.importe
            cajaActual.save()
            super(MovCaja, self).save(*args, **kwargs)
        else:
            return


class OrdenPago(models.Model):
    empresa = models.ForeignKey(Registro)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    personal = models.ForeignKey(User, null=True, blank=True, related_name='Perceptor')
    fPago = models.DateField(default=datetime.datetime.now, verbose_name='Fecha pago')
    fCarga = models.DateTimeField(default=datetime.datetime.now) #No admin
    importe = models.FloatField()
    operador = models.ForeignKey(User, null=True, related_name='Usuario') #No admin
    anulado = models.BooleanField(default=False) #No admin
    aplicado = models.BooleanField(default=False) #No admin
    comentario = models.CharField(max_length=500, null=True, blank=True)
    facturas = models.ManyToManyField(Compra, blank=True)
    # Si es pago en efectivo
    caja = models.ForeignKey(Caja, null=True, blank=True)
    motivo = models.ForeignKey(TipoMovCaja, null=True, blank=True)

    # Botones de acciones
    def acciones(self):
        return format_html(
            '<a class="btn" href="{}" target="_blank" title="Imprimir orden"><i class="icon-print"></i></a>',
            reverse('admin:imprimirOrden', args=[self.pk]),
        )
    acciones.short_description = 'Acciones'
    acciones.allow_tags = True

    def beneficiario(self):
        if self.proveedor:
            return self.proveedor
        else:
            return self.personal


class PagosProveedor(models.Model):
    documento = models.ForeignKey(Compra)
    nroPago = models.IntegerField()
    fPago = models.DateTimeField(auto_now=True)
    importe = models.FloatField()
    ordenPago = models.ForeignKey(OrdenPago)
