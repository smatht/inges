# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0016_auto_20180125_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compraitem',
            name='producto',
        ),
        migrations.AlterField(
            model_name='compra',
            name='afectaStock',
            field=models.BooleanField(default=False, verbose_name=b'Afecta a stock'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='condPago',
            field=models.CharField(default=b'CTD', max_length=3, verbose_name=b'Condici\xc3\xb3n pago', choices=[(b'CTD', b'Contado'), (b'CRE', b'Cr\xc3\xa9dito')]),
        ),
        migrations.AlterField(
            model_name='compra',
            name='esCopia',
            field=models.BooleanField(default=False, verbose_name=b'Es copia'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fContabilizar',
            field=models.DateField(default=datetime.datetime.now, help_text=b'Afecta a informes contables.', verbose_name=b'Fecha contable'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='fDocumento',
            field=models.DateField(verbose_name=b'Fecha del documento'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='numDoc',
            field=models.IntegerField(verbose_name=b'Numero'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='prFinal',
            field=models.BooleanField(default=True, verbose_name=b'Utiliza precio final'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='tipoDoc',
            field=models.ForeignKey(verbose_name=b'Documento', to='mantenimiento.TiposDoc'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='totBruto',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='totDescuentos',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='totImpuestos',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='totNeto',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='compraitem',
            name='cantidad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='compraitem',
            name='precio_unitario',
            field=models.FloatField(),
        ),
    ]
