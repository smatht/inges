# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0032_auto_20180421_1031'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name_plural': 'Compras'},
        ),
        migrations.AlterModelOptions(
            name='compraitem',
            options={'verbose_name': 'Detalle de documento', 'verbose_name_plural': 'Detalle de documento'},
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-fechaPedido'], 'verbose_name': 'Orden de compra', 'verbose_name_plural': 'Ordenes de compra'},
        ),
    ]
