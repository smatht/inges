# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fondos', '0018_auto_20180413_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenpago',
            name='personal',
            field=models.ForeignKey(related_name='Perceptor', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='ordenpago',
            name='operador',
            field=models.ForeignKey(related_name='Usuario', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
