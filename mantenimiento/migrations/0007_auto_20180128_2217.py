# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0006_configuracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracion',
            name='compras_empresa',
            field=models.ForeignKey(related_name='empresaCompra', to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='compras_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacCompra', to='mantenimiento.TiposDoc', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_empresa',
            field=models.ForeignKey(related_name='empresaVenta', to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacVenta', to='mantenimiento.TiposDoc', null=True),
        ),
    ]
