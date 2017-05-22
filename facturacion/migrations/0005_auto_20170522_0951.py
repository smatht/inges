# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_proveedor_nombre_fantasia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emision_factura',
            name='tipo',
            field=models.CharField(default=b'a', max_length=1, choices=[(b'a', b'Factura A'), (b'b', b'Factura B'), (b'c', b'Factura C'), (b'nca', b'Nota de cr\xc3\xa9dito A'), (b'ncb', b'Nota de cr\xc3\xa9dito B')]),
        ),
        migrations.AlterField(
            model_name='registro_factura',
            name='tipo',
            field=models.CharField(default=b'a', max_length=1, choices=[(b'a', b'Factura A'), (b'b', b'Factura B'), (b'c', b'Factura C'), (b'nca', b'Nota de cr\xc3\xa9dito A'), (b'ncb', b'Nota de cr\xc3\xa9dito B')]),
        ),
    ]
