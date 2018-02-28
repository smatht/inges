# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0002_cuenta_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='color',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='montoInicial',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='position',
        ),
    ]
