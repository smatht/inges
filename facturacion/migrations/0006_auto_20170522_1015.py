# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0005_auto_20170522_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='emision_factura',
            name='percepciones_otros',
            field=models.DecimalField(null=True, verbose_name=b'Percepciones de otros', max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='registro_factura',
            name='percepciones_otros',
            field=models.DecimalField(null=True, verbose_name=b'Percepciones de otros', max_digits=6, decimal_places=2, blank=True),
        ),
    ]
