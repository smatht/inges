# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('fondos', '0007_auto_20180211_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='movcaja',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='facturacion.Proveedor', null=True),
        ),
        migrations.AlterField(
            model_name='movcaja',
            name='numDoc',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='movcaja',
            name='tipoDoc',
            field=models.ForeignKey(blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
    ]
