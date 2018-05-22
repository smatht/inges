# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0036_auto_20180515_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='tipoDoc',
            field=models.ForeignKey(verbose_name=b'Documento', to='common.TiposDoc'),
        ),
    ]
