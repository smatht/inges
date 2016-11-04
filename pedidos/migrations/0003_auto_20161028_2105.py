# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20161028_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenretiro_cabecera',
            name='obra',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AlterField(
            model_name='ordenretiro_cabecera',
            name='remitente',
            field=models.ForeignKey(related_name='fromUser', to=settings.AUTH_USER_MODEL, help_text=b'Persona que autoriza'),
        ),
        migrations.AlterField(
            model_name='ordenretiro_cabecera',
            name='se_autoriza',
            field=models.ForeignKey(related_name='toUser', verbose_name=b'Se autoriza a', to=settings.AUTH_USER_MODEL),
        ),
    ]
