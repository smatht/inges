# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10, null=True, blank=True)),
                ('montoInicial', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MovCuenta',
            fields=[
                ('id', models.CharField(max_length=36, serialize=False, primary_key=True)),
                ('importe', models.FloatField()),
                ('tipoPago', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('notas', models.TextField()),
                ('estado', models.CharField(max_length=50)),
                ('categoria', models.ForeignKey(to='fondos_externos.Categoria')),
                ('cuenta', models.ForeignKey(to='fondos_externos.Cuenta')),
            ],
        ),
    ]
