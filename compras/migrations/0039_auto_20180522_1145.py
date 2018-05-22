# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0038_auto_20180522_1114'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='compra',
            table='Compras',
        ),
        migrations.AlterModelTable(
            name='compraitem',
            table='ComprasItems',
        ),
        migrations.AlterModelTable(
            name='compraitemconcepto',
            table='ComprasItemsConceptos',
        ),
        migrations.AlterModelTable(
            name='doccuentaproveedor',
            table='DocCuentaProveedor',
        ),
        migrations.AlterModelTable(
            name='pedido',
            table='Pedidos',
        ),
        migrations.AlterModelTable(
            name='pedidoitem',
            table='PedidosItems',
        ),
        migrations.AlterModelTable(
            name='pedidoitemconcepto',
            table='PedidosItemsConceptos',
        ),
        migrations.AlterModelTable(
            name='remito',
            table='Remitos',
        ),
        migrations.AlterModelTable(
            name='remitoitem',
            table='RemitosItems',
        ),
    ]
