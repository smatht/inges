# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0029_remove_compraitem_obra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compraitemconcepto',
            name='obra',
        ),
    ]
