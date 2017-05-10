# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20170510_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemitoCabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroRemito', models.CharField(max_length=20)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('destino', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='destino',
            field=models.ForeignKey(verbose_name=b'Obra', to='proyectos.Obra'),
        ),
        migrations.AddField(
            model_name='remitocabecera',
            name='pedido',
            field=models.ForeignKey(blank=True, to='pedidos.PedidoCabecera', null=True),
        ),
    ]
