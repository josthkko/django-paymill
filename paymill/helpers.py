# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from .models import Transaction, Client
import pymill


def create_transaction(token, transaction_params, client_params=None):
    """
    * Get or create Client by email.
    * Create Payment.
    * Create Transaction.
    """
    p = pymill.Pymill(settings.PAYMILL_PRIVATE_KEY)

    card_params = {
        'token': token
    }

    if client_params:
        try:
            client = Client.objects.get(email=client_params['email'])
        except Client.DoesNotExist:
            client = Client.update_or_create(client_params)

        transaction_params['client'] = client.id
        card_params['client'] = client.id

    transaction_params['payment'] = p.new_card(**card_params)

    _transaction = p.transact(**transaction_params)
    return Transaction.parse_transaction(_transaction)
