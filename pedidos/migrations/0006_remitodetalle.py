# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_auto_20170510_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemitoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('cantidad', models.CharField(max_length=10)),
                ('medida', models.CharField(default=b'un', max_length=2, choices=[(b'un', b'unidades'), (b'mt', b'metros'), (b'm2', b'metros cuadrados'), (b'm3', b'metros cubicos'), (b'gr', b'gramos'), (b'kg', b'kilogramos'), (b'lt', b'litros'), (b'ml', b'milimetros'), (b'km', b'kil\xc3\xb3metros'), (b'tn', b'toneladas'), (b'om', b'otras medidas')])),
                ('importe', models.DecimalField(max_digits=10, decimal_places=2)),
                ('remito', models.ForeignKey(to='pedidos.RemitoCabecera')),
            ],
        ),
    ]
