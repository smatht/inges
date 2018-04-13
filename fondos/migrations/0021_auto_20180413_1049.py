# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0020_auto_20180413_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenpago',
            name='obra',
        ),
        migrations.RemoveField(
            model_name='ordenpago',
            name='tipoCaja',
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='caja',
            field=models.ForeignKey(blank=True, to='fondos.Caja', null=True),
        ),
    ]
