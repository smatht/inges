# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20170821_2032'),
        ('fondos', '0017_auto_20180413_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenpago',
            name='obra',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AddField(
            model_name='ordenpago',
            name='tipoCaja',
            field=models.ForeignKey(blank=True, to='fondos.TipoCaja', null=True),
        ),
    ]
