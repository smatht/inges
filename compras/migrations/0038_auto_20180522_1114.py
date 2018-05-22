# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0037_auto_20180522_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compraitem',
            name='alicuota',
            field=models.ForeignKey(to='common.Impuesto'),
        ),
        migrations.AlterField(
            model_name='compraitemconcepto',
            name='alicuota',
            field=models.ForeignKey(to='common.Impuesto'),
        ),
    ]
