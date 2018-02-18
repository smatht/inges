# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras', '0025_auto_20180212_1341'),
        ('fondos', '0008_auto_20180212_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fPago', models.DateField(default=datetime.datetime.now, verbose_name=b'Fecha pago')),
                ('fCarga', models.DateTimeField(default=datetime.datetime.now)),
                ('importe', models.FloatField()),
                ('anulado', models.BooleanField(default=False)),
                ('aplicado', models.BooleanField(default=False)),
                ('comentario', models.CharField(max_length=100, null=True, blank=True)),
                ('caja', models.ForeignKey(to='fondos.Caja')),
                ('facturas', models.ManyToManyField(to='compras.Compra', null=True, blank=True)),
                ('operador', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
            ],
        ),
    ]
