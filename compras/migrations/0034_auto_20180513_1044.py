# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0033_auto_20180512_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocCuentaProveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('importeDocumento', models.FloatField()),
                ('importePagado', models.FloatField(default=0)),
                ('importeSaldo', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='compra',
            name='saldo',
        ),
        migrations.AddField(
            model_name='doccuentaproveedor',
            name='documento',
            field=models.ForeignKey(to='compras.Compra'),
        ),
    ]
