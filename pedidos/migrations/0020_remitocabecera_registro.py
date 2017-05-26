# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        ('pedidos', '0019_remitocabecera_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='remitocabecera',
            name='registro',
            field=models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro'),
        ),
    ]
