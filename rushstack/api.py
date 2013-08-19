import logging
from rushstackclient.v1.client import Client as rush_client
from openstack_dashboard.api.base import url_for

from django.conf import settings


LOG = logging.getLogger(__name__)


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def rushclient(request):
    t = request.user.token.id
    url = url_for(request, 'rushstack')
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('rushstackclient connection created using token "%s" and url "%s"'
            % (request.user.token.id, url))
    return rush_client(url, token=t, insecure=insecure)


def get_list(request):
    return rushclient(request).rushes.get_list()

def get_rush_data(request, rush_id):
    rushes_list = get_list(request)
    for item in rushes_list:
        if item.id == rush_id:
            return item

def create(request, rush_type_id, rush_name):
    return rushclient(request).rushes.create(rush_type_id, rush_name)


def delete(request, rush_id):
    return rushclient(request).rushes.delete(rush_id)


