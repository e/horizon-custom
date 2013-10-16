import logging
from novaclient.v1_1 import client as nova_client
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
    # url = 'http://10.95.196.136:21000/v1/' + request.user.tenant_id
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('bigdataclient connection created using token "%s" and url "%s"'
            % (request.user.token.id, url))
    return bigdata_client(url, token=t, insecure=insecure)


def novaclient(request):
    insecure = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
    LOG.debug('novaclient connection created using token "%s" and url "%s"' %
              (request.user.token.id, url_for(request, 'compute')))
    c = nova_client.Client(request.user.username,
                           request.user.token.id,
                           project_id=request.user.tenant_id,
                           auth_url=url_for(request, 'compute'),
                           insecure=insecure,
                           http_log_debug=settings.DEBUG)
    c.client.auth_token = request.user.token.id
    c.client.management_url = url_for(request, 'compute')
    return c


def get_list(request):
    return bigdataclient(request).tdafservice.get_list()


def get_service(request, bigdata_id):
    return bigdataclient(request).tdafservice.get_service(bigdata_id)

def create(request, keypair_name):
    return bigdataclient(request).tdafservice.create(keypair_name)


def delete(request, bigdata_id):
    return bigdataclient(request).tdafservice.delete(bigdata_id)

def get_keypair_list(request):
    return novaclient(request).keypairs.list()
