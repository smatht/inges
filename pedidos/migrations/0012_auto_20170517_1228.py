# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidos', '0011_extenduser_habilitarpedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidocabecera',
            name='firmante',
            field=models.ForeignKey(related_name='fromUser', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Persona que autoriza', null=True),
        ),
        migrations.AlterField(
            model_name='pedidocabecera',
            name='remitente',
            field=models.ForeignKey(related_name='registerUser', to=settings.AUTH_USER_MODEL, help_text=b'Persona que registra'),
        ),
    ]
