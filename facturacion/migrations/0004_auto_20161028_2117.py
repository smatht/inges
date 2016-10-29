# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20161028_2117'),
        ('facturacion', '0003_auto_20161028_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='proveedor',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
