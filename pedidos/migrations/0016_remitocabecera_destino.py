# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20170517_1915'),
        ('pedidos', '0015_auto_20170518_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='remitocabecera',
            name='destino',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
    ]
