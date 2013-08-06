from .workflows import EnableRush
from horizon import tables, workflows
from .tables import RushstackTable
from .api import get_status, get_endpoint, Struct


class IndexView(tables.views.DataTableView):
    table_class = RushstackTable
    template_name = 'project/rushstack/index.html'

    def get_data(self):
        if self.request.is_ajax():
            args = {'id': 1, 'task': 'XXX', 'status': 'misterio'}
            s = Struct(**args)
            data = [s,]
            return data

        args = {}
        rush_id = get_status(self.request)[2]
        if rush_id:
            endpoint = get_endpoint(self.request, rush_id)[1]
            args['rush_id'] = rush_id
            args['id'] = rush_id
            args['size'] = 'Large'
            if endpoint != 'http://:5001':
                args['endpoint'] = endpoint
                args['OS-EXT-STS:task_state'] = None
                args['status'] = 'Enabled'
            else:
                args['endpoint'] = '-'
                args['OS-EXT-STS:task_state'] = 'Provisioning'
                args['status'] = 'Enabling Rush...'

        else:
            endpoint = '-'
            args['rush_id'] = '-'
            args['id'] = 1
            args['size'] = 'Large'
            args['endpoint'] = '-'
            args['OS-EXT-STS:task_state'] = None
            args['status'] = '-'

        s = Struct(**args)
        data = [s,]
        return data

class LaunchRushstackView(workflows.WorkflowView):
    workflow_class = EnableRush


