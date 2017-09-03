# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0009_auto_20170828_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoitem',
            name='unidades',
            field=models.ForeignKey(default=1, to='stock.Unidades'),
        ),
        migrations.AlterField(
            model_name='remitoitem',
            name='unidades',
            field=models.ForeignKey(default=1, to='stock.Unidades'),
        ),
    ]
