# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0017_auto_20180522_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='general_obraCaja',
            field=models.ForeignKey(related_name='obraCaja', verbose_name=b'Obra de caja', blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='general_tipoCaja',
            field=models.ForeignKey(related_name='tipoCaja', verbose_name=b'Tipo de caja', blank=True, to='fondos.TipoCaja', null=True),
        ),
        migrations.AlterModelTable(
            name='configuracion',
            table='Configuraciones',
        ),
    ]
