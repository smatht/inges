# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0005_auto_20180128_1554'),
        ('compras', '0019_remove_compraitem_alicuota'),
    ]

    operations = [
        migrations.AddField(
            model_name='compraitem',
            name='alicuota',
            field=models.ForeignKey(default=1, to='mantenimiento.Impuesto'),
            preserve_default=False,
        ),
    ]
