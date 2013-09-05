from horizon import tables
from django.utils.translation import ugettext_lazy as _
from .api import get_list, get_servdir_data, delete
from django.template.defaultfilters import title
from horizon.utils.filters import replace_underscores

class EnableLink(tables.LinkAction):
    name = "enable"
    verbose_name = _("Enable Service Directory")
    url = "horizon:project:servdirstack:enable"
    classes = ("btn-launch", "ajax-modal")

    def allowed(self, request, datum):
        return True


class DisableLink(tables.BatchAction):
    name = "Disable"
    verbose_name = _("Disable Service Directory")
    action_present = "Disable"
    action_past = "Scheduled termination of"
    data_type_singular =_("Service")
    data_type_plural =_("Services")
    classes = ("btn-danger", "btn-terminate")

    def allowed(self, request, datum):
        return bool(len(get_list(request)))

    def action(self, request, servdir_id):
        delete(request, servdir_id)


class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, servdir_id):
        return get_servdir_data(request, servdir_id)


class ServDirStackTable(tables.DataTable):
    STATUS_CHOICES = (
        ("Create Complete", True),
        ("Create Failed", False),
    )
    SIZE_CHOICES = (
        ("small", "small"),
        ("medium", "medium"),
        ("large", "large"),
    )
    name = tables.Column("name",
                         verbose_name=_("Name"),)
    size = tables.Column("type",
                         verbose_name=_("Size"),)
    status = tables.Column("status",
                         status=True,
                         status_choices=STATUS_CHOICES,
                         filters=(title, replace_underscores),
                         verbose_name=_("Status"),)
    endpoint = tables.Column("endpoint",
                         verbose_name=_("Endpoint"),)

    def get_object_display(self, servdir):
        return servdir.name


    class Meta:
        name = "servdir"
        verbose_name = _("Service Directory")
        table_actions = (EnableLink, DisableLink) 
        status_columns = ["status"]
        row_class = UpdateRow

