import logging
from servdirstackclient.v1.client import Client as servdir_client
from openstack_dashboard.api.base import url_for

from django.conf import settings


LOG = logging.getLogger(__name__)


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def servdirclient(request):
    t = request.user.token.id
    url = url_for(request, 'servdirstack')
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('servdirstackclient connection created using token "%s" and url "%s"'
            % (request.user.token.id, url))
    return servdir_client(url, token=t, insecure=insecure)


def get_list(request):
    return servdirclient(request).servdirs.get_list()

def get_servdir_data(request, servdir_id):
    servdirs_list = get_list(request)
    for item in servdirs_list:
        if item.id == servdir_id:
            return item

def create(request, servdir_type_id, servdir_name):
    return servdirclient(request).servdirs.create(servdir_type_id, servdir_name)


def delete(request, servdir_id):
    return servdirclient(request).servdirs.delete(servdir_id)


