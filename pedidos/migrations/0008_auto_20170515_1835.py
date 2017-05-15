# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20170512_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remitocabecera',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
