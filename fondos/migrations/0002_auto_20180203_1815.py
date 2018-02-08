# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipocaja',
            options={'ordering': ['pk'], 'verbose_name': 'Caja', 'verbose_name_plural': 'Cajas'},
        ),
        migrations.AlterModelOptions(
            name='tipomovcaja',
            options={'ordering': ['pk'], 'verbose_name': 'Tipo movimiento', 'verbose_name_plural': 'Tipo movimiento'},
        ),
        migrations.RemoveField(
            model_name='movcaja',
            name='caja',
        ),
        migrations.AlterField(
            model_name='tipomovcaja',
            name='suma',
            field=models.BooleanField(default=False),
        ),
    ]
