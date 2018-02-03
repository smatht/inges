# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0010_auto_20180202_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='empresa',
            field=models.ForeignKey(verbose_name=b'Empresa principal', blank=True, to='facturacion.Registro', null=True),
        ),
    ]
