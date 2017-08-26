# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_auto_20170825_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-fechaPedido'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='fecha',
            new_name='fechaCarga',
        ),
        migrations.RenameField(
            model_name='remito',
            old_name='fecha',
            new_name='fechaCarga',
        ),
        migrations.AddField(
            model_name='pedido',
            name='fechaPedido',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='remito',
            name='fechaRemito',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='remito',
            name='pedido',
            field=models.ForeignKey(blank=True, to='compras.Pedido', null=True),
        ),
    ]
