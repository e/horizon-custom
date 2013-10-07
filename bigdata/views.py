from .workflows import EnableBigdata
from horizon import tables, workflows, tabs
from .tables import BigdataTable
from .api import get_list, get_service
from .tabs import BigdataTabs


class IndexView(tables.views.DataTableView):
    table_class = BigdataTable
    template_name = 'project/bigdata/index.html'

    def get_data(self):
        return get_list(self.request)

class LaunchBigdataView(workflows.WorkflowView):
    workflow_class = EnableBigdata


class DetailView(tabs.TabView):
    tab_group_class = BigdataTabs
    template_name = 'project/bigdata/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["bigdata"] = self.get_data(self.kwargs.get('instance_id'))
        return context

    def get_data(self, bigdata_id):
        return get_service(self.request, self.kwargs['instance_id'])

    def get_tabs(self, request, *args, **kwargs):
        bigdata = self.get_data(self)
        return self.tab_group_class(request, bigdata=bigdata, **kwargs)

