# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0034_auto_20180513_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fSaldada',
            field=models.DateField(null=True, blank=True),
        ),
    ]
