# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0015_auto_20180304_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='movcaja',
            name='idWallet',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='caja',
            name='idCuentaWallet',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
    ]
