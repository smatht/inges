# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('descripcion_corta', models.CharField(max_length=30, null=True, blank=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('ciudad', models.ForeignKey(blank=True, to='facturacion.Ciudad', null=True)),
                ('cliente', models.ForeignKey(to='facturacion.Cliente')),
                ('localidad', models.ForeignKey(blank=True, to='facturacion.Localidad', null=True)),
                ('pais', models.ForeignKey(blank=True, to='facturacion.Pais', null=True)),
            ],
        ),
    ]
