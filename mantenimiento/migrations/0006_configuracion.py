# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('mantenimiento', '0005_auto_20180128_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('compras_condPago', models.CharField(default=b'CTD', max_length=3, verbose_name=b'Condici\xc3\xb3n pago', choices=[(b'CTD', b'Contado'), (b'CRE', b'Cr\xc3\xa9dito')])),
                ('compras_empresa', models.ForeignKey(related_name='empresaCompra', to='facturacion.Registro')),
                ('compras_tipoDoc', models.ForeignKey(related_name='tipoFacCompra', to='mantenimiento.TiposDoc')),
                ('ventas_empresa', models.ForeignKey(related_name='empresaVenta', to='facturacion.Registro')),
                ('ventas_tipoDoc', models.ForeignKey(related_name='tipoFacVenta', to='mantenimiento.TiposDoc')),
            ],
        ),
    ]
