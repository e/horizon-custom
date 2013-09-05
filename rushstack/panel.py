from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Rushstack(horizon.Panel):
    name = _("Http Relayer")
    slug = "httprelayer"
    # permissions = ('openstack.services.tdaf-service',)

dashboard.Project.register(Rushstack)
