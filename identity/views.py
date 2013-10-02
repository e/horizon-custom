from .workflows import EnableAccounts
from horizon import tables, workflows, tabs
from .tables import AccountsTable
from .api import get_list
from .tabs import AccountsTabs


class IndexView(tables.views.DataTableView):
    table_class = AccountsTable
    template_name = 'project/identity/index.html'

    def get_data(self):
        return get_list(self.request)

class LaunchAccountsView(workflows.WorkflowView):
    workflow_class = EnableAccounts


class DetailView(tabs.TabView):
    tab_group_class = AccountsTabs
    template_name = 'project/identity/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["accounts"] = self.get_data()
        return context

    def get_data(self):
        return self.__dict__

    def get_tabs(self, request, *args, **kwargs):
        identity = self.get_data()
        return self.tab_group_class(request, identity=identity, **kwargs)

