# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0006_auto_20180302_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.CharField(max_length=40, serialize=False, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movcuenta',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='movcuenta',
            name='cuenta',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='id',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='MovCuenta',
        ),
    ]
