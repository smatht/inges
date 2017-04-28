# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Emision_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Emision_factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(default=datetime.datetime.now, help_text=b'Cambie este campo s\xc3\xb3lo en caso de registrar una factura para un mes anterior, tenga en cuenta que al registrar para otro mes \xc3\xa9sta no se incluir\xc3\xa1 en los informes del mes actual.')),
                ('fecha_factura', models.DateField()),
                ('nro_factura', models.CharField(max_length=20)),
                ('tipo', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'A'), (b'b', b'B'), (b'c', b'C')])),
                ('observaciones', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'emisi\xf3n facturas',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domicilio_fiscal', models.CharField(max_length=140, blank=True)),
                ('telefono', models.CharField(max_length=50, blank=True)),
                ('telefono_secundario', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=140)),
                ('cantidad', models.PositiveSmallIntegerField()),
                ('precio_unitario', models.DecimalField(max_digits=10, decimal_places=2)),
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
                ('tipo', models.CharField(default=b'a', max_length=1, choices=[(b'a', b'A'), (b'b', b'B'), (b'c', b'C')])),
                ('observaciones', models.TextField(blank=True)),
                ('pagado', models.BooleanField(default=True)),
                ('esCopia', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'registro facturas',
            },
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
                ('domicilio_comercial', models.CharField(max_length=140, blank=True)),
                ('cuit', models.CharField(max_length=20, blank=True)),
                ('sitio_web', models.CharField(max_length=140, blank=True)),
            ],
            options={
                'ordering': ['razon_social'],
                'verbose_name_plural': 'proveedores',
            },
            bases=('facturacion.empresa',),
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('empresa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='facturacion.Empresa')),
                ('nombre_fantasia', models.CharField(max_length=50, null=True, blank=True)),
                ('razon_social', models.CharField(max_length=50)),
                ('cuit', models.CharField(max_length=20)),
                ('domicilio_comercial', models.CharField(max_length=140)),
                ('iva', models.CharField(default=b'RI', max_length=2, choices=[(b'RI', b'IVA RESPONSABLE INSCRIPTO'), (b'RNI', b'IVA RESPONSABLE NO INSCRIPTO'), (b'RM', b'IVA RESPONSABLE MONOTRIBUTO'), (b'EX', b'IVA SUJETO EXENTO'), (b'NR', b'IVA NO RESPONSABLE')])),
                ('fecha_inicio_actividad', models.DateField(null=True, blank=True)),
                ('membrete', models.ImageField(null=True, upload_to=b'user_img/', blank=True)),
                ('logo', models.ImageField(null=True, upload_to=b'user_img/', blank=True)),
            ],
            options={
                'ordering': ['nombre_fantasia'],
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Registro empresa',
            },
            bases=('facturacion.empresa',),
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='alicuota',
            field=models.ForeignKey(to='facturacion.Iva'),
        ),
        migrations.AddField(
            model_name='factura_detalle',
            name='factura',
            field=models.ForeignKey(to='facturacion.Registro_factura'),
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
    ]
