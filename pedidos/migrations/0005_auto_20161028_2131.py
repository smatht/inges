# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_auto_20161028_2117'),
        ('pedidos', '0004_auto_20161028_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='obra',
        ),
        migrations.AddField(
            model_name='ordenretiro_cabecera',
            name='proveedor',
            field=models.ForeignKey(to='facturacion.Proveedor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordenretiro_cabecera',
            name='destino',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AlterField(
            model_name='ordenretiro_detalle',
            name='cantidad',
            field=models.CharField(max_length=10),
        ),
    ]
