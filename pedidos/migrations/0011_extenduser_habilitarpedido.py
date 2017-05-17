# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_auto_20170516_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='habilitarPedido',
            field=models.BooleanField(default=False, help_text=b'(Marque este campo en caso de que el usuario pueda generar una orden de retiro con su firma)', verbose_name=b'Habilitar orden de retiro'),
        ),
    ]
