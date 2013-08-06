import logging
from rushstackclient.client import Client as rush_client
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
    return rush_client('1', url, token=t, insecure=insecure)


def get_status(request):
    # get_status() -> (result, active, rush_id)
    return rushclient(request).rush.get_status()


def get_endpoint(request, rush_id):
    return rushclient(request).rush.get_endpoint(rush_id)


def create(request, rush_type_id):
    return rushclient(request).rush.create(rush_type_id)


def delete(request, rush_id):
    return rushclient(request).rush.delete(rush_id)


def delete_rush(request):
    rush_id = get_status(request)[2]
    delete(request, rush_id)
    return




