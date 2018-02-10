# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20170821_2032'),
        ('fondos', '0003_auto_20180203_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='destino',
            field=models.ForeignKey(default=1, to='proyectos.Obra'),
            preserve_default=False,
        ),
    ]
