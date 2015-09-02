# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Iva'
        db.create_table(u'facturacion_iva', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('porcentaje', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'facturacion', ['Iva'])

        # Adding model 'Pais'
        db.create_table(u'facturacion_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'facturacion', ['Pais'])

        # Adding model 'Ciudad'
        db.create_table(u'facturacion_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'facturacion', ['Ciudad'])

        # Adding model 'Localidad'
        db.create_table(u'facturacion_localidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'facturacion', ['Localidad'])

        # Adding model 'Empresa_Ente'
        db.create_table(u'facturacion_empresa_ente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('cuit', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('telefono_secundario', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Pais'], null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Ciudad'], null=True, blank=True)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Localidad'], null=True, blank=True)),
        ))
        db.send_create_signal(u'facturacion', ['Empresa_Ente'])

        # Adding model 'Factura_recibida'
        db.create_table(u'facturacion_factura_recibida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrado_el', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nro_factura', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('iva', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Iva'])),
            ('percepciones_otros', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2)),
            ('emisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Empresa_Ente'])),
        ))
        db.send_create_signal(u'facturacion', ['Factura_recibida'])

        # Adding model 'Factura_emitida'
        db.create_table(u'facturacion_factura_emitida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrado_el', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nro_factura', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('subtotal', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('iva', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Iva'])),
            ('percepciones_otros', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2)),
            ('ente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Empresa_Ente'])),
        ))
        db.send_create_signal(u'facturacion', ['Factura_emitida'])

        # Adding model 'Informes'
        db.create_table(u'facturacion_informes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'facturacion', ['Informes'])

        # Adding model 'Albaran_emitido'
        db.create_table(u'facturacion_albaran_emitido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrado_el', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nro_albaran', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('ente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Empresa_Ente'])),
        ))
        db.send_create_signal(u'facturacion', ['Albaran_emitido'])

        # Adding model 'Albaran_recibido'
        db.create_table(u'facturacion_albaran_recibido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrado_el', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nro_albaran', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('emisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Empresa_Ente'])),
        ))
        db.send_create_signal(u'facturacion', ['Albaran_recibido'])


    def backwards(self, orm):
        # Deleting model 'Iva'
        db.delete_table(u'facturacion_iva')

        # Deleting model 'Pais'
        db.delete_table(u'facturacion_pais')

        # Deleting model 'Ciudad'
        db.delete_table(u'facturacion_ciudad')

        # Deleting model 'Localidad'
        db.delete_table(u'facturacion_localidad')

        # Deleting model 'Empresa_Ente'
        db.delete_table(u'facturacion_empresa_ente')

        # Deleting model 'Factura_recibida'
        db.delete_table(u'facturacion_factura_recibida')

        # Deleting model 'Factura_emitida'
        db.delete_table(u'facturacion_factura_emitida')

        # Deleting model 'Informes'
        db.delete_table(u'facturacion_informes')

        # Deleting model 'Albaran_emitido'
        db.delete_table(u'facturacion_albaran_emitido')

        # Deleting model 'Albaran_recibido'
        db.delete_table(u'facturacion_albaran_recibido')


    models = {
        u'facturacion.albaran_emitido': {
            'Meta': {'object_name': 'Albaran_emitido'},
            'ente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Empresa_Ente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nro_albaran': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'registrado_el': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'facturacion.albaran_recibido': {
            'Meta': {'object_name': 'Albaran_recibido'},
            'emisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Empresa_Ente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nro_albaran': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'registrado_el': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'facturacion.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'facturacion.empresa_ente': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Empresa_Ente'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Ciudad']", 'null': 'True', 'blank': 'True'}),
            'cuit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Pais']", 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telefono_secundario': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'facturacion.factura_emitida': {
            'Meta': {'object_name': 'Factura_emitida'},
            'ente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Empresa_Ente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Iva']"}),
            'nro_factura': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'percepciones_otros': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'registrado_el': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'facturacion.factura_recibida': {
            'Meta': {'object_name': 'Factura_recibida'},
            'emisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Empresa_Ente']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iva': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Iva']"}),
            'nro_factura': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'percepciones_otros': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '6', 'decimal_places': '2'}),
            'registrado_el': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'subtotal': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'facturacion.informes': {
            'Meta': {'object_name': 'Informes'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'facturacion.iva': {
            'Meta': {'object_name': 'Iva'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'facturacion.localidad': {
            'Meta': {'object_name': 'Localidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'facturacion.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['facturacion']