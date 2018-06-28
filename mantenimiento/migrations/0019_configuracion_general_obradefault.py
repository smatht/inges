# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_auto_20180522_1145'),
        ('mantenimiento', '0018_auto_20180522_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='general_obraDefault',
            field=models.ForeignKey(related_name='obraDefault', verbose_name=b'Obra por defecto', blank=True, to='proyectos.Obra', null=True),
        ),
    ]
