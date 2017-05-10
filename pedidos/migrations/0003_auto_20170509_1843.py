# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0004_proveedor_nombre_fantasia'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0001_initial'),
        ('pedidos', '0002_auto_20170501_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoCabecera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('destino', models.ForeignKey(blank=True, to='proyectos.Obra', null=True)),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
                ('registro', models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro')),
                ('remitente', models.ForeignKey(related_name='fromUser', to=settings.AUTH_USER_MODEL, help_text=b'Persona que autoriza')),
                ('se_autoriza', models.ForeignKey(related_name='toUser', verbose_name=b'Se autoriza a', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=140)),
                ('orden_retiro', models.ForeignKey(to='pedidos.PedidoCabecera')),
            ],
        ),
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='registro',
        ),
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='remitente',
        ),
        migrations.RemoveField(
            model_name='ordenretiro_cabecera',
            name='se_autoriza',
        ),
        migrations.RemoveField(
            model_name='ordenretiro_detalle',
            name='orden_retiro',
        ),
        migrations.DeleteModel(
            name='OrdenRetiro_cabecera',
        ),
        migrations.DeleteModel(
            name='OrdenRetiro_detalle',
        ),
    ]
