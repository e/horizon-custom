import logging
from bigdataclient.v1.client import Client as bigdata_client
from openstack_dashboard.api.base import url_for

from django.conf import settings


LOG = logging.getLogger(__name__)


class Struct(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


def bigdataclient(request):
    t = request.user.token.id
    url = url_for(request, 'tdaf-bigdata')
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('bigdataclient connection created using token "%s" and url "%s"'
            % (request.user.token.id, url))
    return bigdata_client(url, token=t, insecure=insecure)


def get_list(request):
    return bigdataclient(request).tdafservice.get_list()

def get_service(request, bigdata_id):
    return bigdataclient(request).tdafservice.get_service(bigdata_id)

def create(request, bigdata_type_id, bigdata_name):
    return bigdataclient(request).tdafservice.create( bigdata_name)


def delete(request, bigdata_id):
    return bigdataclient(request).tdafservice.delete(bigdata_id)


