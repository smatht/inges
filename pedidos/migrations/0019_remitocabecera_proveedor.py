# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('pedidos', '0018_remitocabecera_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='remitocabecera',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='facturacion.Proveedor', null=True),
        ),
    ]
