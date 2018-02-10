# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20170821_2032'),
        ('compras', '0021_compraitemconcepto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='obra',
            field=models.ForeignKey(default=1, to='proyectos.Obra'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compraitem',
            name='obra',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AddField(
            model_name='compraitemconcepto',
            name='obra',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
    ]
