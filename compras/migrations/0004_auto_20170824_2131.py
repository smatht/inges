# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_pedido_generaremito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remito',
            name='pedido',
            field=models.ForeignKey(to='compras.Pedido'),
        ),
    ]
