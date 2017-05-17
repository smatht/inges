# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0012_auto_20170517_1228'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidodetalle',
            options={'verbose_name': 'Detalle de pedido', 'verbose_name_plural': 'Detalle de pedido'},
        ),
    ]
