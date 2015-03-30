# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Flatpage'
        db.create_table(u'flatpages_flatpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 3, 8, 0, 0))),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'flatpages', ['Flatpage'])


    def backwards(self, orm):
        # Deleting model 'Flatpage'
        db.delete_table(u'flatpages_flatpage')


    models = {
        u'flatpages.flatpage': {
            'Meta': {'object_name': 'Flatpage'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 3, 8, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['flatpages']