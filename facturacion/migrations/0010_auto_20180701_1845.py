# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ciudad',
            table='Ciudades',
        ),
        migrations.AlterModelTable(
            name='localidad',
            table='Localidades',
        ),
        migrations.AlterModelTable(
            name='pais',
            table='Paises',
        ),
    ]
