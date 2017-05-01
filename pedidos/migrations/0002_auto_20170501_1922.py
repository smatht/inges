# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenretiro_cabecera',
            name='registro',
            field=models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro'),
        ),
    ]
