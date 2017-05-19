# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0013_auto_20170517_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remitodetalle',
            options={'verbose_name': 'Detalle de remito', 'verbose_name_plural': 'Detalle de remito'},
        ),
        migrations.AlterField(
            model_name='remitocabecera',
            name='destino',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='remitocabecera',
            name='fecha',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='remitocabecera',
            name='numeroRemito',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
