# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0002_tiposdoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
                ('valorImpuesto', models.DecimalField(max_digits=5, decimal_places=4)),
                ('esPorcentaje', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoImpuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='impuesto',
            name='tiposImpuesto',
            field=models.ForeignKey(to='mantenimiento.TipoImpuesto'),
        ),
    ]
