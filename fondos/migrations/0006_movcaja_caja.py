# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0005_auto_20180210_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='movcaja',
            name='caja',
            field=models.ForeignKey(default=1, to='fondos.Caja'),
            preserve_default=False,
        ),
    ]
