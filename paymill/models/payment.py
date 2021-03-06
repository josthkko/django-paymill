# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from .base import PaymillModel
from .client import Client


@python_2_unicode_compatible
class Payment(PaymillModel):
    client = models.ForeignKey(Client, related_name='payments')
    type = models.CharField(max_length=20)
    card_type = models.CharField(max_length=10)
    country = models.CharField(max_length=100, blank=True, null=True)
    expire_month = models.PositiveIntegerField()
    expire_year = models.PositiveIntegerField()
    card_holder = models.CharField(max_length=30, blank=True, null=True)
    last4 = models.CharField(max_length=4)

    _token = None

    def __init__(self, *args, **kwargs):
        self._token = kwargs.pop('token', None)
        return super(Payment, self).__init__(*args, **kwargs)

    def _create_paymill_object(self):
        if self._token:
            return self.paymill.new_card(
                self._token,
                client=self.client.id if self.client else None
            )
        return None

    def _delete_paymill_object(self, *args, **kwargs):
        self.paymill.delete_card(self.id)

    def __str__(self):
        return '%s - %s (**** ***** **** %s)' % (self.card_holder,
                                                 self.card_type, self.last4)
