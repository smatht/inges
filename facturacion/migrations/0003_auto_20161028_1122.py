# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0002_auto_20161028_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='unidad_medida',
            field=models.CharField(default=b'un', max_length=3, choices=[(b'un', b'Unidades'), (b'mts', b'Metros'), (b'cm', b'Centimetros'), (b'lts', b'Litro'), (b'kg', b'Kilo'), (b'm3', b'Metro Cubico')]),
        ),
    ]
