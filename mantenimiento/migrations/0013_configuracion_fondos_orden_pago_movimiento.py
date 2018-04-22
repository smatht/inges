# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0012_tipomovcaja'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='fondos_orden_pago_movimiento',
            field=models.ForeignKey(related_name='tipoMovCaja', verbose_name=b'Tipo movimiento de caja', blank=True, to='mantenimiento.TipoMovCaja', null=True),
        ),
    ]
