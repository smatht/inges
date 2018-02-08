# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0002_auto_20180203_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='movcaja',
            name='caja',
            field=models.ForeignKey(default=1, to='fondos.TipoCaja'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movcaja',
            name='tipoMovCaja',
            field=models.ForeignKey(default=1, to='fondos.TipoMovCaja'),
            preserve_default=False,
        ),
    ]
