# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('mantenimiento', '0009_auto_20180202_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='compras_empresa',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='ventas_empresa',
        ),
        migrations.AddField(
            model_name='configuracion',
            name='empresa',
            field=models.ForeignKey(blank=True, to='facturacion.Registro', null=True),
        ),
    ]
