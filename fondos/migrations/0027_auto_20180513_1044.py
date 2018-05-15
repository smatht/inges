# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0026_doccuentaproveedor_pagosproveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doccuentaproveedor',
            name='documento',
        ),
        migrations.DeleteModel(
            name='DocCuentaProveedor',
        ),
    ]
