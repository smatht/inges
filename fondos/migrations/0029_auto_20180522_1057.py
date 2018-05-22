# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0028_pagosproveedor_importe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movcaja',
            name='tipoDoc',
            field=models.ForeignKey(verbose_name=b'Tipo de documento', blank=True, to='common.TiposDoc', null=True),
        ),
    ]
