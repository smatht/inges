# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20170428_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura_detalle',
            name='impuesto',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='registro_factura',
            name='registro',
            field=models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro'),
        ),
    ]
