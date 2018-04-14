# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0028_auto_20180319_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compraitem',
            name='obra',
        ),
    ]
