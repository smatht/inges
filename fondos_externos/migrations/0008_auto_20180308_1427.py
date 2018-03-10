# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0007_auto_20180308_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='accountId',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='amount',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='categoryId',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='currencyId',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='registro',
            name='note',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='paymentType',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='registro',
            name='recordState',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
