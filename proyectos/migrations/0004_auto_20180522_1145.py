# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20170821_2032'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='obra',
            table='Obras',
        ),
    ]
