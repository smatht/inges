# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0005_auto_20180128_1554'),
        ('compras', '0020_compraitem_alicuota'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompraItemConcepto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('cantidad', models.FloatField()),
                ('precio_unitario', models.FloatField()),
                ('alicuota', models.ForeignKey(to='mantenimiento.Impuesto')),
                ('factura', models.ForeignKey(to='compras.Compra')),
            ],
            options={
                'verbose_name': 'Concepto',
                'verbose_name_plural': 'Conceptos',
            },
        ),
    ]
