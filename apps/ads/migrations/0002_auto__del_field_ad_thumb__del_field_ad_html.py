# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting field 'Ad.thumb'
        db.delete_column(u'ads_ad', 'thumb')

        # Deleting field 'Ad.html'
        db.delete_column(u'ads_ad', 'html')


    def backwards(self, orm):
        # Adding field 'Ad.thumb'
        db.add_column(u'ads_ad', 'thumb',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ad.html'
        db.add_column(u'ads_ad', 'html',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


    models = {
        u'ads.ad': {
            'Meta': {'ordering': "('priority', 'id')", 'object_name': 'Ad'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'section': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ads']