# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0011_auto_20170908_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remito',
            old_name='origen',
            new_name='iOrigen',
        ),
        migrations.RenameField(
            model_name='remito',
            old_name='numeroRemito',
            new_name='sNumeroRemito',
        ),
        migrations.RenameField(
            model_name='remito',
            old_name='observaciones',
            new_name='sObservaciones',
        ),
        migrations.RemoveField(
            model_name='remito',
            name='afectaStock',
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='sAclaracion',
            field=models.CharField(max_length=50, null=True, verbose_name=b'aclaracion', blank=True),
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='sCantidad',
            field=models.CharField(default=b'1', max_length=10, verbose_name=b'cantidad'),
        ),
    ]
