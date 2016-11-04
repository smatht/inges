# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenRetiro_cabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('destino', models.ForeignKey(to='facturacion.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenRetiro_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=4, decimal_places=2)),
                ('descripcion', models.ForeignKey(to='facturacion.Material')),
                ('orden_retiro', models.ForeignKey(to='pedidos.OrdenRetiro_cabecera')),
            ],
        ),
    ]
