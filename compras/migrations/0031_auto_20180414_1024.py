# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0030_remove_compraitemconcepto_obra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='afectaCaja',
            field=models.BooleanField(default=True, verbose_name=b'Generar mov. caja'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='afectaStock',
            field=models.BooleanField(default=True, verbose_name=b'Afecta a stock'),
        ),
    ]
