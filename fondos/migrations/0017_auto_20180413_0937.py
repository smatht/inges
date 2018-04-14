# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0016_auto_20180312_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenpago',
            name='caja',
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='proveedor',
            field=models.ForeignKey(blank=True, to='facturacion.Proveedor', null=True),
        ),
    ]
