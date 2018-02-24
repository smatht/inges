# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0012_auto_20180222_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movcaja',
            name='numDoc',
            field=models.IntegerField(null=True, verbose_name=b'Numero de documento', blank=True),
        ),
        migrations.AlterField(
            model_name='movcaja',
            name='tipoDoc',
            field=models.ForeignKey(verbose_name=b'Tipo de documento', blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
    ]
