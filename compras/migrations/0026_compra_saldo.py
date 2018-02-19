# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0025_auto_20180212_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='saldo',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
