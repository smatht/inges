# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170827_2145'),
        ('compras', '0007_auto_20170827_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidoitem',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='remitoitem',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.RemoveField(
            model_name='pedidoitem',
            name='importe',
        ),
        migrations.RemoveField(
            model_name='pedidoitem',
            name='precioUnitario',
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='unidades',
            field=models.ForeignKey(default=1, to='stock.Unidades'),
            preserve_default=False,
        ),
    ]
