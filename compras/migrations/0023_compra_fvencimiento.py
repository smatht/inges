# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0022_auto_20180210_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='fVencimiento',
            field=models.DateField(default=datetime.datetime(2018, 2, 11, 15, 9, 46, 148477, tzinfo=utc), verbose_name=b'Fecha de vencimiento'),
            preserve_default=False,
        ),
    ]
