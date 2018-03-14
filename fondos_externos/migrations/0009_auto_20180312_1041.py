# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0008_auto_20180308_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='note',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='recordState',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
