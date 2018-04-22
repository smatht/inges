# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0013_configuracion_fondos_orden_pago_movimiento'),
        ('fondos', '0023_auto_20180421_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenpago',
            name='motivo',
            field=models.ForeignKey(blank=True, to='mantenimiento.TipoMovCaja', null=True),
        ),
    ]
