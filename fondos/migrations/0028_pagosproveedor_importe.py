# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0027_auto_20180513_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagosproveedor',
            name='importe',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
