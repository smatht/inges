# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fondos_externos', '0006_auto_20180302_1116'),
        ('fondos', '0013_auto_20180224_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='cuentaWallet',
            field=models.ForeignKey(verbose_name=b'Cuenta Wallet', blank=True, to='fondos_externos.Cuenta', null=True),
        ),
    ]
