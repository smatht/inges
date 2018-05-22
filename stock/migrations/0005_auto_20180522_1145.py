# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20180222_1130'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='familia',
            table='Familias',
        ),
        migrations.AlterModelTable(
            name='linea',
            table='Lineas',
        ),
        migrations.AlterModelTable(
            name='preciocompra',
            table='PreciosCompra',
        ),
        migrations.AlterModelTable(
            name='producto',
            table='Productos',
        ),
        migrations.AlterModelTable(
            name='unidades',
            table='Unidades',
        ),
    ]
