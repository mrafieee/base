# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'congress_member')

        # Deleting model 'Fee'
        db.delete_table(u'congress_fee')

        # Adding field 'Congress.fee'
        db.add_column('congress', 'fee',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'congress_member', (
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_member', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('receipt', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('job_id_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('office_address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('hospital', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('paid_fee', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
            ('registration_date', self.gf('django.db.models.fields.CharField')(default='1', max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Iran', max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'congress', ['Member'])

        # Adding model 'Fee'
        db.create_table(u'congress_fee', (
            ('fee', self.gf('django.db.models.fields.TextField')()),
            ('workshop_fee', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
        ))
        db.send_create_signal(u'congress', ['Fee'])

        # Deleting field 'Congress.fee'
        db.delete_column('congress', 'fee')


    models = {
        u'congress.article': {
            'Meta': {'object_name': 'Article'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'abstract_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'main_topic': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'postal_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'congress.boarddirectory': {
            'Meta': {'object_name': 'BoardDirectory'},
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'congress.congress': {
            'Meta': {'object_name': 'Congress', 'db_table': "'congress'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'closing_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 3, 23, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'early_registration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '6'}),
            'late_registration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'online_registration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'opening_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 3, 23, 0, 0)'}),
            'paramedics_articles_abstract': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'physician_articles_abstract': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poster': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'registration_fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'registration_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sessions_program': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'venue': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'congress.media': {
            'Meta': {'ordering': "('file',)", 'object_name': 'Media'},
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumb': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['congress']