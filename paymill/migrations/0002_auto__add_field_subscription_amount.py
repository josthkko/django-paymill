# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subscription.amount'
        db.add_column(u'paymill_subscription', 'amount',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Subscription.amount'
        db.delete_column(u'paymill_subscription', 'amount')


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
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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