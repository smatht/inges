# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0027_auto_20180222_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='idCaja',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fVencimiento',
            field=models.DateField(default=datetime.datetime.now, verbose_name=b'Fecha de vencimiento'),
        ),
    ]
