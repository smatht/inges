# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mantenimiento', '0011_auto_20180203_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fApertura', models.DateTimeField(default=datetime.datetime.now)),
                ('fCierre', models.DateTimeField(null=True, blank=True)),
                ('montoInicial', models.FloatField(default=0)),
                ('acumEntradas', models.FloatField(null=True, blank=True)),
                ('acumSalidas', models.FloatField(null=True, blank=True)),
                ('empresa', models.ForeignKey(to='facturacion.Registro')),
            ],
        ),
        migrations.CreateModel(
            name='MovCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('numDoc', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('importe', models.FloatField()),
                ('caja', models.ForeignKey(to='fondos.Caja')),
                ('operador', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('tipoDoc', models.ForeignKey(to='mantenimiento.TiposDoc')),
            ],
            options={
                'verbose_name': 'Movimiento de caja',
                'verbose_name_plural': 'Movimientos de caja',
            },
        ),
        migrations.CreateModel(
            name='TipoCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Cajas',
            },
        ),
        migrations.CreateModel(
            name='TipoMovCaja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=75)),
                ('suma', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Tipo movimiento',
                'verbose_name_plural': 'Tipo movimiento',
            },
        ),
        migrations.AddField(
            model_name='caja',
            name='tipoCaja',
            field=models.ForeignKey(to='fondos.TipoCaja'),
        ),
    ]
