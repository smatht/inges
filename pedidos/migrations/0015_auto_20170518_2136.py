# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0014_auto_20170518_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remitocabecera',
            name='destino',
        ),
        migrations.AlterField(
            model_name='remitocabecera',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
