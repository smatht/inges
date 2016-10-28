# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unidad_medida',
            field=models.CharField(default=b'un', max_length=2, choices=[(b'un', b'Unidades'), (b'mts', b'Metros'), (b'cm', b'Centimetros'), (b'lts', b'Litro'), (b'kg', b'Kilo'), (b'm3', b'Metro Cubico')]),
        ),
        migrations.DeleteModel(
            name='UnidadMedida',
        ),
    ]
