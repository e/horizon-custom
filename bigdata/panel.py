from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Bigdata(horizon.Panel):
    name = _("Big Data")
    slug = "bigdata"
    # permissions = ('openstack.services.tdaf-service',)

dashboard.Project.register(Bigdata)
