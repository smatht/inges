# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('descripcionCorta', models.CharField(max_length=10)),
                ('activo', models.BooleanField(default=True)),
                ('familia', models.ForeignKey(to='stock.Familia')),
                ('proveedor', models.ManyToManyField(to='facturacion.Proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=20)),
                ('descripcionCorta', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.ForeignKey(to='stock.Unidades'),
        ),
        migrations.AddField(
            model_name='familia',
            name='linea',
            field=models.ForeignKey(to='stock.Linea'),
        ),
    ]
