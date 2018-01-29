# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0007_auto_20180128_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='compras_empresa',
            field=models.ForeignKey(related_name='empresaCompra', blank=True, to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='compras_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacCompra', blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_empresa',
            field=models.ForeignKey(related_name='empresaVenta', blank=True, to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacVenta', blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
    ]
