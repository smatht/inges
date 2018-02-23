# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0026_compra_saldo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='condPago',
            field=models.CharField(default=b'CTD', max_length=3, verbose_name=b'Condicion pago', choices=[(b'CTD', b'Contado'), (b'CRE', b'Cr\xc3\xa9dito')]),
        ),
    ]
