# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0039_auto_20180522_1145'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='compra',
            unique_together=set([('tipoDoc', 'sucursal', 'numDoc', 'proveedor')]),
        ),
    ]
