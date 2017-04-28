# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
        ('facturacion', '0002_auto_20170428_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenRetiro_cabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('destino', models.ForeignKey(blank=True, to='proyectos.Obra', null=True)),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
                ('registro', models.ForeignKey(verbose_name=b'Empresa', to='facturacion.Registro')),
                ('remitente', models.ForeignKey(related_name='fromUser', to=settings.AUTH_USER_MODEL, help_text=b'Persona que autoriza')),
                ('se_autoriza', models.ForeignKey(related_name='toUser', verbose_name=b'Se autoriza a', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orden de retiro',
                'verbose_name_plural': 'Ordenes de retiro',
            },
        ),
        migrations.CreateModel(
            name='OrdenRetiro_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=140)),
                ('orden_retiro', models.ForeignKey(to='pedidos.OrdenRetiro_cabecera')),
            ],
        ),
    ]
