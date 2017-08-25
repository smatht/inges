# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20170824_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='generaRemito',
            field=models.BooleanField(default=False, verbose_name=b'Recepci\xc3\xb3n inmediata'),
        ),
    ]
