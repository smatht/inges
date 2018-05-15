# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0013_configuracion_fondos_orden_pago_movimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='compras_tipoMovCajaDef',
            field=models.ForeignKey(related_name='tipoMovCajaCompra', verbose_name=b'Tipo Mov Caja por defecto', blank=True, to='mantenimiento.TipoMovCaja', null=True),
        ),
    ]
