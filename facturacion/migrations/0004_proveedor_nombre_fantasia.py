# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20170501_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='nombre_fantasia',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
