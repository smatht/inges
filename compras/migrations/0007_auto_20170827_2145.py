# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170827_2145'),
        ('compras', '0006_auto_20170825_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoitem',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='producto',
            field=models.ForeignKey(default=1, to='stock.Producto'),
            preserve_default=False,
        ),
    ]
