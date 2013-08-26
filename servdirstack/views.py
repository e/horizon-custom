from .workflows import EnableServDir
from horizon import tables, workflows
from .tables import ServDirStackTable
from .api import get_list


class IndexView(tables.views.DataTableView):
    table_class = ServDirStackTable
    template_name = 'project/servdirstack/index.html'

    def get_data(self):
        return get_list(self.request)

class LaunchServDirStackView(workflows.WorkflowView):
    workflow_class = EnableServDir


