from django.utils.translation import ugettext_lazy as _

from horizon import exceptions, tabs


class DetailsTab(tabs.Tab):
    name = _("Details")
    slug="details"
    template_name = ("project/identity/_details.html")

    def get_context_data(self, request):
        return {"identity": self.tab_group.kwargs['identity']}


class AccountsTabs(tabs.TabGroup):
    slug = "identity_details"
    tabs = (DetailsTab,)
    sticky = True
