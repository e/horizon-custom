from django.utils.translation import ugettext_lazy as _

from horizon import exceptions, tabs


class DetailsTab(tabs.Tab):
    name = _("Details")
    slug="details"
    template_name = ("project/bigdata/_bigdata_details.html")

    def get_context_data(self, request):
        return {"bigdata": self.tab_group.kwargs['instance_id']}


class AnotherTab(tabs.Tab):
    name = _("Additional Data")
    slug="additional_data"
    template_name = ("project/bigdata/_additional_data.html")

    def get_context_data(self, request):
        return {"bigdata": self.tab_group.kwargs['instance_id']}



class BigdataTabs(tabs.TabGroup):
    slug = "bigdata_details"
    tabs = (DetailsTab, AnotherTab)
    sticky = True
