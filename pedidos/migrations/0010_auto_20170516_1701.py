# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_auto_20170516_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidodetalle',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]
