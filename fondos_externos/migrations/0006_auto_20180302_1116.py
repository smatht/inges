# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0005_auto_20180302_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10, null=True, blank=True)),
                ('excludeFromStats', models.BooleanField()),
                ('gps', models.BooleanField()),
                ('initAmount', models.FloatField(default=0)),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='movcuenta',
            name='cuenta',
            field=models.ForeignKey(default=1, to='fondos_externos.Cuenta'),
            preserve_default=False,
        ),
    ]
