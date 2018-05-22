# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0030_auto_20180522_1114'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='caja',
            table='Cajas',
        ),
        migrations.AlterModelTable(
            name='movcaja',
            table='MovsCaja',
        ),
        migrations.AlterModelTable(
            name='ordenpago',
            table='OrdenesPago',
        ),
        migrations.AlterModelTable(
            name='pagosproveedor',
            table='PagosProveedor',
        ),
        migrations.AlterModelTable(
            name='tipocaja',
            table='TiposCaja',
        ),
    ]
