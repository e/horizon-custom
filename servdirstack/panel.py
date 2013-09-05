from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class ServDirStack(horizon.Panel):
    name = _("Service Directory")
    slug = "servdirstack"
    # permissions = ('openstack.services.tdaf-service',)

dashboard.Project.register(ServDirStack)
