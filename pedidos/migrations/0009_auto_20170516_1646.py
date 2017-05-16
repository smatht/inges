# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_auto_20170515_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remitodetalle',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]
