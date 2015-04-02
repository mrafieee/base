# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Congress'
        db.create_table('congress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('is_open', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('opening_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 3, 23, 0, 0))),
            ('closing_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 3, 23, 0, 0))),
            ('registration_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('registration_fax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('early_registration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('late_registration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('online_registration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('venue', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('physician_articles_abstract', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('paramedics_articles_abstract', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('sessions_program', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'congress', ['Congress'])

        # Adding model 'BoardDirectory'
        db.create_table(u'congress_boarddirectory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'congress', ['BoardDirectory'])

        # Adding model 'Member'
        db.create_table(u'congress_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Iran', max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_member', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('job_id_number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hospital', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('office_address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('registration_date', self.gf('django.db.models.fields.CharField')(default='1', max_length=100)),
            ('paid_fee', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('receipt', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'congress', ['Member'])

        # Adding model 'Article'
        db.create_table(u'congress_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('postal_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('main_topic', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abstract_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'congress', ['Article'])

        # Adding model 'Fee'
        db.create_table(u'congress_fee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'])),
            ('fee', self.gf('django.db.models.fields.TextField')()),
            ('workshop_fee', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'congress', ['Fee'])

        # Adding model 'Media'
        db.create_table(u'congress_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('thumb', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('congress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['congress.Congress'], null=True, blank=True)),
        ))
        db.send_create_signal(u'congress', ['Media'])


    def backwards(self, orm):
        # Deleting model 'Congress'
        db.delete_table('congress')

        # Deleting model 'BoardDirectory'
        db.delete_table(u'congress_boarddirectory')

        # Deleting model 'Member'
        db.delete_table(u'congress_member')

        # Deleting model 'Article'
        db.delete_table(u'congress_article')

        # Deleting model 'Fee'
        db.delete_table(u'congress_fee')

        # Deleting model 'Media'
        db.delete_table(u'congress_media')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        u'congress.fee': {
            'Meta': {'object_name': 'Fee'},
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']"}),
            'fee': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'workshop_fee': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'congress.media': {
            'Meta': {'ordering': "('file',)", 'object_name': 'Media'},
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumb': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'congress.member': {
            'Meta': {'object_name': 'Member'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'congress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['congress.Congress']"}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Iran'", 'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hospital': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_member': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'job_id_number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'office_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'paid_fee': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'receipt': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'registration_date': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['congress']