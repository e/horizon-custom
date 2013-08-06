from horizon import tables
from django.utils.translation import ugettext_lazy as _
from .api import get_status, get_endpoint, delete_rush, Struct



class EnableLink(tables.LinkAction):
    name = "enable"
    verbose_name = _("Enable Rush")
    url = "horizon:project:rushstack:enable"
    classes = ("btn-launch", "ajax-modal")

    def allowed(self, request, datum):
        return not get_status(request)[1]


class DisableLink(tables.BatchAction):
    name = "Disable"
    verbose_name = _("Disable Rush")
    action_present = "Disable"
    action_past = "Scheduled termination of"
    data_type_singular =_("Service")
    data_type_plural =_("Services")
    classes = ("btn-danger", "btn-terminate")

    def allowed(self, request, datum):
        # get_status() -> (result, active, rush_id)
        return get_status(request)[1]

    def action(self, request, obj_id):
        delete_rush(request)


class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, obj_id):
        rush_id = get_status(request)[2]
        d = {'id': 1,
             'rush_id': rush_id,
             'size': 'Large',
             'OS-EXT-STS:task_state': 'Spawning',
             'endpoint': '-',
             'status': 'Enabling Rush...'}
        if rush_id:
            d['id'] = rush_id
            e = get_endpoint(request, rush_id)[1]
            if e == 'http://:5001':
                d['OS-EXT-STS:task_state'] = 'Provisioning'
                d['status'] = 'Finalizing'
                d['endpoint'] = '-'
            else:
                d['OS-EXT-STS:task_state'] = None
                d['status'] = 'Enabled'
                d['endpoint'] = e
        else:
            d['size'] = '-'
            d['OS-EXT-STS:task_state'] = None
            d['status'] = 'Disabled'
            d['endpoint'] = '-'

        obj = Struct(**d)
        return obj


class RushstackTable(tables.DataTable):
    TASK_DISPLAY_CHOICES = (
        ("image_snapshot", "Snapshotting"),
        ("resize_prep", "Preparing Resize or Migrate"),
        ("resize_migrating", "Resizing or Migrating"),
        ("resize_migrated", "Resized or Migrated"),
        ("resize_finish", "Finishing Resize or Migrate"),
        ("resize_confirming", "Confirming Resize or Nigrate"),
        ("resize_reverting", "Reverting Resize or Migrate"),
        ("unpausing", "Resuming"),
    )
    TASK_STATUS_CHOICES = (
        (None, True),
        ("none", True)
    )
    STATUS_CHOICES = (
        ("active", True),
        ("not active", True),
    )
    SIZE_CHOICES = (
        ("small", "small"),
        ("medium", "medium"),
        ("large", "large"),
    )
    rush_id = tables.Column("rush_id",
                         verbose_name=_("Rush ID"),)
    size = tables.Column("size",
                         verbose_name=_("Size"),)
                         #choices=SIZE_CHOICES)
    status = tables.Column("status",
                          verbose_name=_("Status"),)
    task = tables.Column("OS-EXT-STS:task_state",
                         verbose_name=_("Task"),
                        # filters=(title, replace_underscores),
                         status='unknown',
                         status_choices=TASK_STATUS_CHOICES,
                         display_choices=TASK_DISPLAY_CHOICES)
    endpoint = tables.Column("endpoint",
                         verbose_name=_("Endpoint"),)

    def get_object_display(self, obj):
        return "Rush"


    class Meta:
        name = "rush"
        verbose_name = _("Rush")
        table_actions = (EnableLink, DisableLink) 
        status_columns = ["status", "task"]
        row_class = UpdateRow


