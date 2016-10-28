# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emision_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now, help_text=b'Cambie este campo s\xc3\xb3lo en caso de registrar una factura para un mes anterior, tenga en cuenta que al registrar para otro mes \xc3\xa9sta no se incluir\xc3\xa1 en los informes del mes actual.')),
                ('fecha_factura', models.DateField()),
                ('nro_factura', models.CharField(max_length=20)),
                ('percepciones_otros', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('detalle', models.TextField(blank=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'emisi\xf3n facturas',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=140, blank=True)),
                ('telefono', models.CharField(max_length=50, blank=True)),
                ('telefono_secundario', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'permissions': (('can_view_informe', 'Can view informe'),),
            },
        ),
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('ciudad', models.ForeignKey(to='facturacion.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now, help_text=b'Cambie este campo s\xc3\xb3lo en caso de registrar una albaran para un mes anterior, tenga en cuenta que al registrar para otro mes \xc3\xa9ste no se incluir\xc3\xa1 en los informes del mes actual.')),
                ('fecha_recibo', models.DateField()),
                ('nro_recibo', models.CharField(max_length=15, blank=True)),
                ('detalle', models.TextField(blank=True)),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Registro_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now, help_text=b'Cambie este campo s\xc3\xb3lo en caso de registrar una factura para un mes anterior, tenga en cuenta que al registrar para otro mes \xc3\xa9sta no se incluir\xc3\xa1 en los informes del mes actual.')),
                ('fecha_factura', models.DateField()),
                ('nro_factura', models.CharField(max_length=20)),
                ('percepciones_otros', models.DecimalField(default=0, max_digits=6, decimal_places=2)),
                ('detalle', models.TextField(blank=True)),
                ('subtotal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('pagado', models.BooleanField(default=True)),
                ('esCopia', models.BooleanField(default=False)),
                ('iva', models.ForeignKey(to='facturacion.Iva')),
            ],
            options={
                'verbose_name_plural': 'registro facturas',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=20)),
                ('abrr', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('empresa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='facturacion.Empresa')),
                ('nombre', models.CharField(max_length=75)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('cuil', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'ordering': ['nombre'],
            },
            bases=('facturacion.empresa',),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('empresa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='facturacion.Empresa')),
                ('razon_social', models.CharField(max_length=75)),
                ('cuit', models.CharField(max_length=20, blank=True)),
                ('sitio_web', models.CharField(max_length=140, blank=True)),
            ],
            options={
                'ordering': ['razon_social'],
                'verbose_name_plural': 'proveedores',
            },
            bases=('facturacion.empresa',),
        ),
        migrations.AddField(
            model_name='material',
            name='unidad_medida',
            field=models.ForeignKey(to='facturacion.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ciudad',
            field=models.ForeignKey(blank=True, to='facturacion.Ciudad', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='localidad',
            field=models.ForeignKey(blank=True, to='facturacion.Localidad', null=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.ForeignKey(blank=True, to='facturacion.Pais', null=True),
        ),
        migrations.AddField(
            model_name='emision_factura',
            name='iva',
            field=models.ForeignKey(to='facturacion.Iva'),
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
            model_name='recibo',
            name='emisor',
            field=models.ForeignKey(to='facturacion.Proveedor'),
        ),
        migrations.AddField(
            model_name='material',
            name='proveedor',
            field=models.ForeignKey(to='facturacion.Proveedor'),
        ),
        migrations.AddField(
            model_name='emision_factura',
            name='cliente',
            field=models.ForeignKey(to='facturacion.Cliente'),
        ),
    ]
