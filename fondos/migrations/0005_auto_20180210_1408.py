# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('fondos', '0004_caja_destino'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='movcaja',
            name='caja',
        ),
        migrations.AddField(
            model_name='movcaja',
            name='empresa',
            field=models.ForeignKey(default=1, to='facturacion.Registro'),
            preserve_default=False,
        ),
    ]
