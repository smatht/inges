# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0004_auto_20180127_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impuesto',
            name='tipoImpuesto',
            field=models.SmallIntegerField(choices=[(0, b'Impuesto interno'), (1, b'IVA'), (2, b'DGR'), (3, b'Otro')]),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='valorImpuesto',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tiposdoc',
            name='aplicaStock',
            field=models.SmallIntegerField(verbose_name=b'Cambia stock', choices=[(1, b'Aumenta'), (-1, b'Disminuye'), (0, b'No aplica')]),
        ),
        migrations.AlterField(
            model_name='tiposdoc',
            name='id',
            field=models.CharField(max_length=3, serialize=False, verbose_name=b'Nombre', primary_key=True),
        ),
        migrations.AlterField(
            model_name='tiposdoc',
            name='tipo',
            field=models.SmallIntegerField(choices=[(0, b'Factura de venta'), (1, b'Factura de compra'), (2, b'Presupuesto'), (3, b'Otro documento')]),
        ),
    ]
