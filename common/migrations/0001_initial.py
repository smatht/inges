# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposDoc',
            fields=[
                ('id', models.CharField(max_length=3, serialize=False, verbose_name=b'Nombre', primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('esFactura', models.BooleanField(default=False)),
                ('aplicaStock', models.SmallIntegerField(verbose_name=b'Cambia stock', choices=[(1, b'Aumenta'), (-1, b'Disminuye'), (0, b'No aplica')])),
                ('tipo', models.SmallIntegerField(choices=[(0, b'Factura de venta'), (1, b'Factura de compra'), (2, b'Presupuesto'), (3, b'Otro documento')])),
            ],
            options={
                'db_table': 'TiposDoc',
            },
        ),
    ]
