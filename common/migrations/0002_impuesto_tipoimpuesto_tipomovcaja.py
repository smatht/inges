# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('tipoImpuesto', models.SmallIntegerField(choices=[(0, b'Impuesto interno'), (1, b'IVA'), (2, b'DGR'), (3, b'Otro')])),
                ('valorImpuesto', models.FloatField()),
                ('esPorcentaje', models.BooleanField(default=True)),
                ('esObligatorio', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Impuestos',
            },
        ),
        migrations.CreateModel(
            name='TipoImpuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TiposImpuesto',
            },
        ),
        migrations.CreateModel(
            name='TipoMovCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=75)),
                ('suma', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['pk'],
                'db_table': 'TiposMovCaja',
                'verbose_name': 'Tipo movimiento',
                'verbose_name_plural': 'Tipo movimiento',
            },
        ),
    ]
