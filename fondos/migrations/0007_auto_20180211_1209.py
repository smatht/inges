# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0006_movcaja_caja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movcaja',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Fecha y hora'),
        ),
        migrations.AlterField(
            model_name='movcaja',
            name='tipoMovCaja',
            field=models.ForeignKey(verbose_name=b'Operacion', to='fondos.TipoMovCaja'),
        ),
    ]
