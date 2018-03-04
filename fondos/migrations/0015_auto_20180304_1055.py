# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0014_caja_cuentawallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='cuentaWallet',
        ),
        migrations.AddField(
            model_name='caja',
            name='idCuentaWallet',
            field=models.CharField(max_length=36, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='caja',
            name='nombreCuentaWallet',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='movcaja',
            name='origen',
            field=models.SmallIntegerField(default=0),
        ),
    ]
