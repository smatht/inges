# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0015_auto_20180124_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='pagado',
        ),
        migrations.RemoveField(
            model_name='compraitem',
            name='prFinal',
        ),
        migrations.AddField(
            model_name='compra',
            name='afectaStock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='compra',
            name='cai',
            field=models.BigIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='condPago',
            field=models.CharField(default=b'CTD', max_length=3, choices=[(b'CTD', b'Contado'), (b'CRE', b'Cr\xc3\xa9dito')]),
        ),
        migrations.AddField(
            model_name='compra',
            name='prFinal',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='vCai',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fContabilizar',
            field=models.DateField(help_text=b'Afecta a informes contables.', null=True, verbose_name=b'Fecha contable', blank=True),
        ),
    ]
