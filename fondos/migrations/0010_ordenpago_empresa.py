# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('fondos', '0009_ordenpago'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenpago',
            name='empresa',
            field=models.ForeignKey(default=1, to='facturacion.Registro'),
            preserve_default=False,
        ),
    ]
