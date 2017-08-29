# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170827_2145'),
        ('compras', '0008_auto_20170827_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remitoitem',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='remitoitem',
            name='producto',
            field=models.ForeignKey(default=1, to='stock.Producto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='remitoitem',
            name='unidades',
            field=models.ForeignKey(default=1, to='stock.Unidades'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fechaPedido',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'Fecha'),
        ),
    ]
