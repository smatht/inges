# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0015_auto_20180522_1038'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='impuesto',
            table='Impuestos',
        ),
        migrations.AlterModelTable(
            name='tipoimpuesto',
            table='TiposImpuesto',
        ),
        migrations.AlterModelTable(
            name='tipomovcaja',
            table='TiposMovCaja',
        ),
    ]
