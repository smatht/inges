# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0010_auto_20170903_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='anulado',
            new_name='bAnulado',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='generaRemito',
            new_name='bGeneraRemito',
        ),
        migrations.RenameField(
            model_name='pedidoitem',
            old_name='cantidad',
            new_name='sCantidad',
        ),
        migrations.RemoveField(
            model_name='remitoitem',
            name='importe',
        ),
        migrations.RemoveField(
            model_name='remitoitem',
            name='precioUnitario',
        ),
        migrations.AddField(
            model_name='pedidoitem',
            name='sAclaracion',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
