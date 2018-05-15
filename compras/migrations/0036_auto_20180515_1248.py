# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0035_compra_fsaldada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fSaldada',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
