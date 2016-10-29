# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20161028_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenretiro_detalle',
            name='descripcion',
            field=models.CharField(max_length=140),
        ),
    ]
