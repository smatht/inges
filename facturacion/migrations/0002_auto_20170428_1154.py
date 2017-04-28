# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facturacion', '0001_initial'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emision_factura',
            name='obra',
            field=models.ForeignKey(blank=True, to='proyectos.Obra', null=True),
        ),
        migrations.AddField(
            model_name='emision_factura',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='emision_detalle',
            name='alicuota',
            field=models.ForeignKey(to='facturacion.Iva'),
        ),
        migrations.AddField(
            model_name='emision_detalle',
            name='factura',
            field=models.ForeignKey(to='facturacion.Emision_factura'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='pais',
            field=models.ForeignKey(to='facturacion.Pais'),
        ),
        migrations.AddField(
            model_name='registro_factura',
            name='emisor',
            field=models.ForeignKey(to='facturacion.Proveedor'),
        ),
        migrations.AddField(
            model_name='registro_factura',
            name='registro',
            field=models.ForeignKey(verbose_name=b'Empresa', to='facturacion.Registro'),
        ),
        migrations.AddField(
            model_name='recibo',
            name='emisor',
            field=models.ForeignKey(to='facturacion.Proveedor'),
        ),
        migrations.AddField(
            model_name='emision_factura',
            name='cliente',
            field=models.ForeignKey(to='facturacion.Cliente'),
        ),
    ]
