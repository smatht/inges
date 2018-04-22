# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0031_auto_20180414_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fRegistro',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Fecha de carga'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numDoc',
            field=models.IntegerField(verbose_name=b'N\xc3\xbamero'),
        ),
    ]
