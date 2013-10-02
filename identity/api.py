import logging
from accountsclient.v1.client import Client as accounts_client
from openstack_dashboard.api.base import url_for

from django.conf import settings


LOG = logging.getLogger(__name__)


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def accountsclient(request):
    t = request.user.token.id
    url = url_for(request, 'account')
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('accountsclient connection created using token "%s" and url "%s"'
            % (request.user.token.id, url))
    return accounts_client(url, token=t, insecure=insecure)


def get_list(request):
    return accountsclient(request).accounts.get_list()

def get_accounts_data(request, accounts_id):
    accounts_list = get_list(request)
    for item in accounts_list:
        if item.id == accounts_id:
            return item

def create(request, accounts_type_id, accounts_name):
    return accountsclient(request).accounts.create(accounts_type_id, accounts_name)


def delete(request, accounts_id):
    return accountsclient(request).accounts.delete(accounts_id)


