# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Empresa_Ente.email'
        db.add_column(u'facturacion_empresa_ente', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Empresa_Ente.sitio_web'
        db.add_column(u'facturacion_empresa_ente', 'sitio_web',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=140, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Empresa_Ente.email'
        db.delete_column(u'facturacion_empresa_ente', 'email')

        # Deleting field 'Empresa_Ente.sitio_web'
        db.delete_column(u'facturacion_empresa_ente', 'sitio_web')


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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Localidad']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['facturacion.Pais']", 'null': 'True', 'blank': 'True'}),
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