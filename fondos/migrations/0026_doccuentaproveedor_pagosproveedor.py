# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0033_auto_20180512_1342'),
        ('fondos', '0025_auto_20180422_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocCuentaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('importeDocumento', models.FloatField()),
                ('importePagado', models.FloatField()),
                ('importeSaldo', models.FloatField()),
                ('documento', models.ForeignKey(to='compras.Compra')),
            ],
        ),
        migrations.CreateModel(
            name='PagosProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nroPago', models.IntegerField()),
                ('fPago', models.DateTimeField(auto_now=True)),
                ('documento', models.ForeignKey(to='compras.Compra')),
                ('ordenPago', models.ForeignKey(to='fondos.OrdenPago')),
            ],
        ),
    ]
