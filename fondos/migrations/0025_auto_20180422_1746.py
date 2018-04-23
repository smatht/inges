# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0024_ordenpago_motivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenpago',
            name='comentario',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
