# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0024_preciocompra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preciocompra',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='preciocompra',
            name='proveedor',
        ),
        migrations.DeleteModel(
            name='PrecioCompra',
        ),
    ]
