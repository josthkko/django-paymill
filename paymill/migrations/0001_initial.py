# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'paymill_client', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'paymill', ['Client'])

        # Adding model 'Payment'
        db.create_table(u'paymill_payment', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'payments', to=orm['paymill.Client'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('card_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('expire_month', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('expire_year', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('card_holder', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('last4', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'paymill', ['Payment'])

        # Adding model 'Offer'
        db.create_table(u'paymill_offer', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('interval', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('trial_period_days', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'paymill', ['Offer'])

        # Adding model 'Subscription'
        db.create_table(u'paymill_subscription', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('livemode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cancel_at_period_end', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('trial_start', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('trial_end', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('next_capture_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('canceled_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('offer', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'subscriptions', to=orm['paymill.Offer'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'subscriptions', to=orm['paymill.Client'])),
            ('payment', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'subscriptions', to=orm['paymill.Payment'])),
        ))
        db.send_create_signal(u'paymill', ['Subscription'])

        # Adding model 'Transaction'
        db.create_table(u'paymill_transaction', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('response_code', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('livemode', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('origin_amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('payment', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'transactions', to=orm['paymill.Payment'])),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'transactions', to=orm['paymill.Client'])),
        ))
        db.send_create_signal(u'paymill', ['Transaction'])

        # Adding model 'Refund'
        db.create_table(u'paymill_refund', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=80, primary_key=True, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('response_code', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('transaction', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'refunds', to=orm['paymill.Transaction'])),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('livemode', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'paymill', ['Refund'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'paymill_client')

        # Deleting model 'Payment'
        db.delete_table(u'paymill_payment')

        # Deleting model 'Offer'
        db.delete_table(u'paymill_offer')

        # Deleting model 'Subscription'
        db.delete_table(u'paymill_subscription')

        # Deleting model 'Transaction'
        db.delete_table(u'paymill_transaction')

        # Deleting model 'Refund'
        db.delete_table(u'paymill_refund')


    models = {
        u'paymill.client': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Client'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'paymill.offer': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Offer'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'trial_period_days': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'paymill.payment': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Payment'},
            'card_holder': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'card_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'payments'", 'to': u"orm['paymill.Client']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'expire_month': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'expire_year': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'last4': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'paymill.refund': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Refund'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {}),
            'response_code': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'transaction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'refunds'", 'to': u"orm['paymill.Transaction']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'paymill.subscription': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Subscription'},
            'cancel_at_period_end': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'canceled_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'subscriptions'", 'to': u"orm['paymill.Client']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'next_capture_at': ('django.db.models.fields.DateTimeField', [], {}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'subscriptions'", 'to': u"orm['paymill.Offer']"}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'subscriptions'", 'to': u"orm['paymill.Payment']"}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'trial_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'trial_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'paymill.transaction': {
            'Meta': {'ordering': "[u'-created_at']", 'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transactions'", 'to': u"orm['paymill.Client']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '80', 'primary_key': 'True', 'db_index': 'True'}),
            'livemode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'origin_amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'payment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'transactions'", 'to': u"orm['paymill.Payment']"}),
            'response_code': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['paymill']