# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0009_auto_20170523_1950'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mantenimiento', '0003_auto_20180124_0948'),
        ('compras', '0014_pedidoitemconcepto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sucursal', models.IntegerField()),
                ('numDoc', models.IntegerField()),
                ('fDocumento', models.DateField()),
                ('fRegistro', models.DateTimeField(default=datetime.datetime.now)),
                ('observaciones', models.TextField(null=True, blank=True)),
                ('anulado', models.BooleanField(default=False)),
                ('fanulacion', models.DateTimeField(null=True, blank=True)),
                ('totBruto', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('totImpuestos', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('totDescuentos', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('totNeto', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('pagado', models.BooleanField(default=False)),
                ('esCopia', models.BooleanField(default=False)),
                ('yaAfectoStock', models.BooleanField(default=False)),
                ('fContabilizar', models.DateField(help_text=b'Afecta a informescontables.', null=True, verbose_name=b'Fecha contable', blank=True)),
                ('afectaEmpresa', models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro')),
                ('operador', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
                ('tipoDoc', models.ForeignKey(to='mantenimiento.TiposDoc')),
            ],
            options={
                'verbose_name_plural': 'registro facturas',
            },
        ),
        migrations.CreateModel(
            name='CompraItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto', models.CharField(max_length=140)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('precio_unitario', models.DecimalField(max_digits=10, decimal_places=2)),
                ('prFinal', models.BooleanField(default=True)),
                ('alicuota', models.ForeignKey(to='mantenimiento.Impuesto')),
                ('factura', models.ForeignKey(to='compras.Compra')),
            ],
            options={
                'verbose_name': 'Detalle de factura',
                'verbose_name_plural': 'Detalle de factura',
            },
        ),
        migrations.AlterField(
            model_name='pedidoitem',
            name='sAclaracion',
            field=models.CharField(max_length=150, null=True, verbose_name=b'aclaracion', blank=True),
        ),
    ]
