# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0021_auto_20180413_1049'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tipomovcaja',
            table='mantenimiento_tipomovcaja',
        ),
    ]
