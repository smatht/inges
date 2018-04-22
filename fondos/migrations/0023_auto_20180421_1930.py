# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos', '0022_auto_20180421_1759'),
        ('mantenimiento', '0012_tipomovcaja'),
    ]

    state_operations = [
        migrations.AlterField(
            model_name='movcaja',
            name='tipoMovCaja',
            field=models.ForeignKey(verbose_name=b'Operacion', to='mantenimiento.TipoMovCaja'),
        ),
        migrations.DeleteModel(
            name='TipoMovCaja',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
