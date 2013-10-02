from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.project import dashboard


class Accounts(horizon.Panel):
    name = _("Identity & Profile")
    slug = "identity"
    # permissions = ('openstack.services.tdaf-service',)

dashboard.Project.register(Accounts)
