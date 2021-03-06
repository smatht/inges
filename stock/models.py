# -*- coding: utf-8 -*-
import datetime
from django.db import models

from facturacion.models import Proveedor



class Unidades(models.Model):
    descripcion = models.CharField(max_length=20)
    descripcionCorta = models.CharField(max_length=5)

    def __unicode__(self):
        return unicode(self.descripcion + ' (' + self.descripcionCorta + ')')

    class Meta:
        db_table = 'Unidades'


class Linea(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        db_table = 'Lineas'


class Familia(models.Model):
    linea = models.ForeignKey(Linea)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.descripcion)

    class Meta:
        db_table = 'Familias'



class Producto(models.Model):
    descripcion = models.CharField(max_length=150)
    descripcionCorta = models.CharField(max_length=10, blank=True, null=True)
    familia = models.ForeignKey(Familia)
    proveedor = models.ManyToManyField(Proveedor)
    unidad = models.ForeignKey(Unidades)
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'Productos'

    def __unicode__(self):
        return unicode(self.descripcion)

    def precio(self, proveedor=None):
        p = PrecioCompra.getPrecioXProductoUltimaVigencia(self, proveedor)
        if p:
            return p.precioCompra
        else:
            return None

    def nuevoPrecio(self, proveedor, precio):
        if proveedor is None:
            p = PrecioCompra(producto=self, precioCompra=precio)
        else:
            p = PrecioCompra(producto=self, proveedor=proveedor, precioCompra=precio)
        p.save()
        # PrecioCompra.setNuevoPrecio(self, proveedor, precio)


class PrecioCompra(models.Model):
    producto = models.ForeignKey(Producto)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    fDesde = models.DateTimeField(default=datetime.datetime.now)
    precioCompra = models.FloatField()

    class Meta:
        db_table = 'PreciosCompra'

    def __unicode__(self):
        return unicode(self.producto.descripcion + " $" + str(self.precioCompra))

    @staticmethod
    def getPrecioXProductoUltimaVigencia(producto, proveedor):
        p = PrecioCompra.objects.filter(producto=producto, proveedor=proveedor)
        if p:
            return p.latest('fDesde')
        else:
            return None
