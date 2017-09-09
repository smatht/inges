# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0012_auto_20170908_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remitoitem',
            old_name='confirmacion',
            new_name='bConfirmacion',
        ),
        migrations.RenameField(
            model_name='remitoitem',
            old_name='cantidad',
            new_name='sCantidad',
        ),
    ]
