# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0029_auto_20180522_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movcaja',
            name='tipoMovCaja',
            field=models.ForeignKey(verbose_name=b'Operacion', to='common.TipoMovCaja'),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='motivo',
            field=models.ForeignKey(blank=True, to='common.TipoMovCaja', null=True),
        ),
    ]
