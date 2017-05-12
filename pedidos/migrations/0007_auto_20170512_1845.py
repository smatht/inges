# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0006_remitodetalle'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedidocabecera',
            options={'ordering': ['-fecha'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='remitocabecera',
            options={'verbose_name': 'Remito', 'verbose_name_plural': 'Remitos'},
        ),
        migrations.AlterModelOptions(
            name='remitodetalle',
            options={'verbose_name': 'Detalle', 'verbose_name_plural': 'Detalle'},
        ),
        migrations.AddField(
            model_name='remitodetalle',
            name='confirmacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='remitodetalle',
            name='importe',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
