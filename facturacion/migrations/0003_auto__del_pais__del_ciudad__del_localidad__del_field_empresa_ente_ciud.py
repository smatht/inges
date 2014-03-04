# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Pais'
        db.delete_table(u'facturacion_pais')

        # Deleting model 'Ciudad'
        db.delete_table(u'facturacion_ciudad')

        # Deleting model 'Localidad'
        db.delete_table(u'facturacion_localidad')

        # Deleting field 'Empresa_Ente.ciudad'
        db.delete_column(u'facturacion_empresa_ente', 'ciudad_id')

        # Deleting field 'Empresa_Ente.pais'
        db.delete_column(u'facturacion_empresa_ente', 'pais_id')

        # Deleting field 'Empresa_Ente.localidad'
        db.delete_column(u'facturacion_empresa_ente', 'localidad_id')


    def backwards(self, orm):
        # Adding model 'Pais'
        db.create_table(u'facturacion_pais', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'facturacion', ['Pais'])

        # Adding model 'Ciudad'
        db.create_table(u'facturacion_ciudad', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'facturacion', ['Ciudad'])

        # Adding model 'Localidad'
        db.create_table(u'facturacion_localidad', (
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'facturacion', ['Localidad'])

        # Adding field 'Empresa_Ente.ciudad'
        db.add_column(u'facturacion_empresa_ente', 'ciudad',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Ciudad'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Empresa_Ente.pais'
        db.add_column(u'facturacion_empresa_ente', 'pais',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Pais'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Empresa_Ente.localidad'
        db.add_column(u'facturacion_empresa_ente', 'localidad',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['facturacion.Localidad'], null=True, blank=True),
                      keep_default=False)


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
        u'facturacion.empresa_ente': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Empresa_Ente'},
            'cuit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'sitio_web': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['facturacion']