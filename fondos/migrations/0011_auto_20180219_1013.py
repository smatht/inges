# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0010_ordenpago_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenpago',
            name='facturas',
            field=models.ManyToManyField(to='compras.Compra', blank=True),
        ),
    ]
