# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0011_auto_20180219_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caja',
            name='acumEntradas',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='caja',
            name='acumSalidas',
            field=models.FloatField(default=0),
        ),
    ]
