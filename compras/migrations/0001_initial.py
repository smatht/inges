# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20170821_2032'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facturacion', '0009_auto_20170523_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(default=datetime.datetime.now)),
                ('destino', models.ForeignKey(verbose_name=b'Obra', to='proyectos.Obra')),
                ('firmante', models.ForeignKey(related_name='fromUser1', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Persona que autoriza', null=True)),
                ('proveedor', models.ForeignKey(to='facturacion.Proveedor')),
                ('registro', models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro')),
                ('remitente', models.ForeignKey(related_name='registerUser1', to=settings.AUTH_USER_MODEL, help_text=b'Persona que registra')),
                ('se_autoriza', models.ForeignKey(related_name='toUser1', verbose_name=b'Se autoriza a', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('cantidad', models.CharField(max_length=10)),
                ('precioUnitario', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('importe', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('pedido', models.ForeignKey(to='compras.Pedido')),
            ],
            options={
                'verbose_name': 'Detalle de pedido',
                'verbose_name_plural': 'Detalle de pedido',
            },
        ),
        migrations.CreateModel(
            name='Remito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numeroRemito', models.CharField(max_length=20, null=True, verbose_name=b'Numero remito', blank=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('destino', models.ForeignKey(blank=True, to='proyectos.Obra', null=True)),
                ('factura', models.ForeignKey(blank=True, to='facturacion.Registro_factura', null=True)),
                ('pedido', models.ForeignKey(blank=True, to='compras.Pedido', null=True)),
                ('proveedor', models.ForeignKey(blank=True, to='facturacion.Proveedor', null=True)),
                ('registro', models.ForeignKey(default=1, verbose_name=b'Empresa', to='facturacion.Registro')),
            ],
            options={
                'verbose_name': 'Remito',
                'verbose_name_plural': 'Remitos',
            },
        ),
        migrations.CreateModel(
            name='RemitoItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmacion', models.BooleanField(default=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('cantidad', models.CharField(max_length=10)),
                ('precioUnitario', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('importe', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('remito', models.ForeignKey(to='compras.Remito')),
            ],
            options={
                'verbose_name': 'Detalle de remito',
                'verbose_name_plural': 'Detalle de remito',
            },
        ),
    ]
