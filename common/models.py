from django.db import models


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


class TipoImpuesto(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'TiposImpuesto'


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
