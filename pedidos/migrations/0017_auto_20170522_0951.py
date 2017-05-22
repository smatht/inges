# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0016_remitocabecera_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remitocabecera',
            name='numeroRemito',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Numero remito', blank=True),
        ),
    ]
