# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_impuesto_tipoimpuesto_tipomovcaja'),
        ('compras', '0040_auto_20180628_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImpuestoXCompra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('importe_neto', models.FloatField()),
                ('factura', models.ForeignKey(to='compras.Compra')),
                ('impuesto', models.ForeignKey(to='common.Impuesto')),
            ],
            options={
                'db_table': 'ImpuestoXCompra',
                'verbose_name': 'Otro impuesto',
                'verbose_name_plural': 'Otros impuestos',
            },
        ),
    ]
