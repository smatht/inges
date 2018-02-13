# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('stock', '0002_auto_20170827_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fDesde', models.DateTimeField(default=datetime.datetime.now)),
                ('precioCompra', models.FloatField()),
                ('producto', models.ForeignKey(to='stock.Producto')),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
            ],
        ),
    ]
