# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0004_auto_20180225_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movcuenta',
            name='cuenta',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
    ]
