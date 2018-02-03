# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimiento', '0008_auto_20180129_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='compras_FacAfectaStk',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='compras_usaPrFinal',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='compras_empresa',
            field=models.ForeignKey(related_name='empresaCompra', verbose_name=b'Empresa', blank=True, to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='compras_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacCompra', verbose_name=b'Tipo doc', blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_empresa',
            field=models.ForeignKey(related_name='empresaVenta', verbose_name=b'Empresa', blank=True, to='facturacion.Registro', null=True),
        ),
        migrations.AlterField(
            model_name='configuracion',
            name='ventas_tipoDoc',
            field=models.ForeignKey(related_name='tipoFacVenta', verbose_name=b'Tipo doc', blank=True, to='mantenimiento.TiposDoc', null=True),
        ),
    ]
