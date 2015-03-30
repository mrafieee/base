# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Ad'
        db.create_table(u'ads_ad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('section', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('html', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='en', max_length=6)),
        ))
        db.send_create_signal(u'ads', ['Ad'])


    def backwards(self, orm):
        # Deleting model 'Ad'
        db.delete_table(u'ads_ad')


    models = {
        u'ads.ad': {
            'Meta': {'ordering': "('priority', 'id')", 'object_name': 'Ad'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'section': ('django.db.models.fields.IntegerField', [], {}),
            'thumb': (
            'django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ads']