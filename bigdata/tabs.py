from django.utils.translation import ugettext_lazy as _

from horizon import exceptions, tabs


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug="overview"
    template_name = ("project/bigdata/_detail_overview.html")

    def get_context_data(self, request):
        data = self.tab_group.kwargs['bigdata']['config']
        return {"bigdata":     data['id'],
                "api_secret":  data['api_secret'],
                "ext_data":    data['extdata'],
                "ssk_pub_key": data['ssk_pub_key'],
                "api_key":     data['api_key'],
                "url":         data['url'],}


class LogTab(tabs.Tab):
    name = _("Log")
    slug="log"
    template_name = ("project/bigdata/_detail_log.html")

    def get_context_data(self, request):
        return {"bigdata": self.tab_group.kwargs['instance_id']}



class BigdataTabs(tabs.TabGroup):
    slug = "bigdata_details"
    tabs = (OverviewTab, LogTab)
    sticky = True
