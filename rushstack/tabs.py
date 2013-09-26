from django.utils.translation import ugettext_lazy as _

from horizon import exceptions, tabs


class DetailsTab(tabs.Tab):
    name = _("Details")
    slug="details"
    template_name = ("project/httprelayer/_details.html")

    def get_context_data(self, request):
        return {"httprelayer": self.tab_group.kwargs['httprelayer']}


class HttpRelayerTabs(tabs.TabGroup):
    slug = "httprelayer_details"
    tabs = (DetailsTab,)
    sticky = True
