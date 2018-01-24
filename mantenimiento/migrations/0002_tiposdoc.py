# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposDoc',
            fields=[
                ('id', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('esFactura', models.BooleanField(default=False)),
            ],
        ),
    ]
