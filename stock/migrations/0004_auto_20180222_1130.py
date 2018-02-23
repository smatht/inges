# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_preciocompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preciocompra',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='facturacion.Proveedor', null=True),
        ),
    ]
