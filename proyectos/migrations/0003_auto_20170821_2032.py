# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20170517_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='descripcion',
            field=models.TextField(max_length=300, verbose_name=b'Obra'),
        ),
    ]
