# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('habilitarPedido', models.BooleanField(default=False, help_text=b'(Marque este campo en caso de que el usuario pueda generar una orden de retiro con su firma)', verbose_name=b'Habilitar orden de retiro')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
