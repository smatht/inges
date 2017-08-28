# -*- coding: utf-8 -*-

from django.db import models

from facturacion.models import Proveedor


class Unidades(models.Model):
    descripcion = models.CharField(max_length=20)
    descripcionCorta = models.CharField(max_length=5)

    def __unicode__(self):
        return unicode(self.descripcion + ' (' + self.descripcionCorta + ')')
    # UNIDAD_MEDIDA = (
    #     ('un', 'unidades'),
    #     ('mt', 'metros'),
    #     ('m²', 'metros cuadrados'),
    #     ('m³', 'metros cubicos'),
    #     ('gr', 'gramos'),
    #     ('kg', 'kilogramos'),
    #     ('lt', 'litros'),
    #     ('ml', 'milimetros'),
    #     ('km', 'kilómetros'),
    #     ('tn', 'toneladas'),
    #     ('om', 'otras medidas'),
    # )
    # medida = models.CharField(
    #     max_length=2,
    #     choices=UNIDAD_MEDIDA,
    #     default='un',
    # )


class Linea(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.descripcion)


class Familia(models.Model):
    linea = models.ForeignKey(Linea)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.descripcion)


class Producto(models.Model):
    descripcion = models.CharField(max_length=150)
    descripcionCorta = models.CharField(max_length=10, blank=True, null=True)
    familia = models.ForeignKey(Familia)
    proveedor = models.ManyToManyField(Proveedor)
    unidad = models.ForeignKey(Unidades)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.descripcion)
