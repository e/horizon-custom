from .workflows import EnableRush
from horizon import tables, workflows, tabs
from .tables import RushstackTable
from .api import get_list
from .tabs import HttpRelayerTabs


class IndexView(tables.views.DataTableView):
    table_class = RushstackTable
    template_name = 'project/httprelayer/index.html'

    def get_data(self):
        return get_list(self.request)

class LaunchRushstackView(workflows.WorkflowView):
    workflow_class = EnableRush


class DetailView(tabs.TabView):
    tab_group_class = HttpRelayerTabs
    template_name = 'project/httprelayer/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["rush"] = self.get_data()
        return context

    def get_data(self):
        return self.__dict__

    def get_tabs(self, request, *args, **kwargs):
        httprelayer = self.get_data()
        return self.tab_group_class(request, httprelayer=httprelayer, **kwargs)

