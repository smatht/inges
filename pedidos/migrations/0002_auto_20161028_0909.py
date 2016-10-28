# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenretiro_cabecera',
            name='obra',
            field=models.ForeignKey(to='proyectos.Obra'),
        ),
        migrations.AddField(
            model_name='ordenretiro_cabecera',
            name='remitente',
            field=models.ForeignKey(related_name='fromUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordenretiro_cabecera',
            name='se_autoriza',
            field=models.ForeignKey(related_name='toUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
