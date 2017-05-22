# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0007_auto_20170522_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='numero_serie',
            field=models.IntegerField(null=True, verbose_name=b'Numero de serie', blank=True),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipo',
            field=models.CharField(default=b'e', max_length=1, choices=[(b'e', b'Efectivo'), (b'c', b'Cheque'), (b't', b'Tarjeta')]),
        ),
        migrations.AlterField(
            model_name='emision_factura',
            name='tipo',
            field=models.CharField(default=b'a', max_length=3, choices=[(b'a', b'Factura A'), (b'b', b'Factura B'), (b'c', b'Factura C'), (b'nca', b'Nota de cr\xc3\xa9dito A'), (b'ncb', b'Nota de cr\xc3\xa9dito B')]),
        ),
        migrations.AlterField(
            model_name='pago',
            name='comprobantes',
            field=models.ManyToManyField(to='facturacion.Registro_factura', blank=True),
        ),
        migrations.AlterField(
            model_name='registro_factura',
            name='tipo',
            field=models.CharField(default=b'a', max_length=3, choices=[(b'a', b'Factura A'), (b'b', b'Factura B'), (b'c', b'Factura C'), (b'nca', b'Nota de cr\xc3\xa9dito A'), (b'ncb', b'Nota de cr\xc3\xa9dito B')]),
        ),
    ]
