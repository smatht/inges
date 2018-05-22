# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0030_auto_20180522_1114'),
        ('proyectos', '0003_auto_20170821_2032'),
        ('mantenimiento', '0016_auto_20180522_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='general_obraCaja',
            field=models.ForeignKey(related_name='obraCaja', blank=True, to='proyectos.Obra', help_text=b'Obra por defecto para realizaci\xc3\xb3n de operaciones de caja', null=True, verbose_name=b'Obra de caja'),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='general_tipoCaja',
            field=models.ForeignKey(related_name='tipoCaja', blank=True, to='fondos.TipoCaja', help_text=b'Tipo de caja por defecto para todo tipo de operacion', null=True, verbose_name=b'Tipo de caja'),
        ),
    ]
