# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0006_auto_20170522_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_recibo', models.DateField()),
                ('nro_recibo', models.CharField(max_length=15, blank=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('observaciones', models.TextField(blank=True)),
                ('comprobantes', models.ManyToManyField(to='facturacion.Registro_factura')),
                ('receptor', models.ForeignKey(to='facturacion.Proveedor')),
            ],
        ),
        migrations.RemoveField(
            model_name='recibo',
            name='emisor',
        ),
        migrations.DeleteModel(
            name='Recibo',
        ),
    ]
