# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170827_2145'),
        ('compras', '0013_auto_20170908_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoItemConcepto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sDescripcion', models.CharField(max_length=300, verbose_name=b'descripcion')),
                ('sCantidad', models.CharField(default=b'1', max_length=10, verbose_name=b'cantidad')),
                ('pedido', models.ForeignKey(to='compras.Pedido')),
                ('unidades', models.ForeignKey(default=1, to='stock.Unidades')),
            ],
            options={
                'verbose_name': 'Concepto',
                'verbose_name_plural': 'Conceptos',
            },
        ),
    ]
