# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0008_auto_20170522_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='factura_detalle',
            options={'verbose_name': 'Detalle de factura', 'verbose_name_plural': 'Detalle de factura'},
        ),
        migrations.RenameField(
            model_name='pago',
            old_name='fecha_recibo',
            new_name='fecha_pago',
        ),
        migrations.AlterField(
            model_name='registro_factura',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]
