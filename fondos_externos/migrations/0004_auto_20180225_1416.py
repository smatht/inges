# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0003_auto_20180225_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='color',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='excludeFromStats',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='gps',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='initAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cuenta',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuenta',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
