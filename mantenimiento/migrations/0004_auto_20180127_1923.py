# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0003_auto_20180124_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impuesto',
            name='tiposImpuesto',
        ),
        migrations.AddField(
            model_name='impuesto',
            name='esObligatorio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='impuesto',
            name='tipoImpuesto',
            field=models.SmallIntegerField(default=1, max_length=1, choices=[(0, b'Impuesto interno'), (1, b'Iva'), (2, b'DGR'), (3, b'Otro')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiposdoc',
            name='aplicaStock',
            field=models.SmallIntegerField(default=0, max_length=2, choices=[(1, b'Aumenta'), (-1, b'Disminuye'), (0, b'No aplica')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiposdoc',
            name='tipo',
            field=models.SmallIntegerField(default=0, max_length=1, choices=[(0, b'Factura de venta'), (1, b'Factura de compra'), (2, b'Presupuesto'), (3, b'Otro documento')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='esPorcentaje',
            field=models.BooleanField(default=True),
        ),
    ]
