# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0014_configuracion_compras_tipomovcajadef'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tiposdoc',
            table='TiposDoc',
        ),
    ]
