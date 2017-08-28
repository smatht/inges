# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcionCorta',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
