# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0019_auto_20180413_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenpago',
            name='tipoCaja',
            field=models.ForeignKey(verbose_name=b'Caja', blank=True, to='fondos.TipoCaja', null=True),
        ),
    ]
