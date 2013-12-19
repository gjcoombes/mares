# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Machine'
        db.create_table(u'runsets_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('cpu_count', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('cpu_frequency', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ram', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('team', self.gf('django.db.models.fields.CharField')(default='NN', max_length=2)),
            ('drives', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'runsets', ['Machine'])

        # Adding model 'RunSet'
        db.create_table(u'runsets_runset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('machine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['runsets.Machine'])),
            ('phase', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=192, blank=True)),
        ))
        db.send_create_signal(u'runsets', ['RunSet'])


    def backwards(self, orm):
        # Deleting model 'Machine'
        db.delete_table(u'runsets_machine')

        # Deleting model 'RunSet'
        db.delete_table(u'runsets_runset')


    models = {
        u'runsets.machine': {
            'Meta': {'object_name': 'Machine'},
            'abbrev': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'cpu_count': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'cpu_frequency': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'drives': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'ram': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'team': ('django.db.models.fields.CharField', [], {'default': "'NN'", 'max_length': '2'})
        },
        u'runsets.runset': {
            'Meta': {'object_name': 'RunSet'},
            'group': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '192', 'blank': 'True'}),
            'machine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['runsets.Machine']"}),
            'phase': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['runsets']