from .workflows import EnableRush
from horizon import tables, workflows
from .tables import RushstackTable
from .api import get_list


class IndexView(tables.views.DataTableView):
    table_class = RushstackTable
    template_name = 'project/httprelayer/index.html'

    def get_data(self):
        return get_list(self.request)

class LaunchRushstackView(workflows.WorkflowView):
    workflow_class = EnableRush


