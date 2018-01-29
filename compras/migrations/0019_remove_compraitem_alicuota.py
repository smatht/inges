# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_compraitem_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compraitem',
            name='alicuota',
        ),
    ]
