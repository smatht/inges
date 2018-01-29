# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20170827_2145'),
        ('compras', '0017_auto_20180128_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraitem',
            name='producto',
            field=models.ForeignKey(default=1, to='stock.Producto'),
            preserve_default=False,
        ),
    ]
