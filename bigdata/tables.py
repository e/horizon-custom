from django.core import urlresolvers
from horizon import tables
from django.utils.translation import ugettext_lazy as _
from .api import get_list, get_service, delete
from django.template.defaultfilters import title
from horizon.utils.filters import replace_underscores


class EnableLink(tables.LinkAction):
    name = "enable"
    verbose_name = _("Enable Big Data Service")
    url = "horizon:project:bigdata:enable"
    classes = ("btn-launch", "ajax-modal")

    def allowed(self, request, datum):
        return True


class DisableLink(tables.BatchAction):
    name = "Disable"
    verbose_name = _("Disable Big Data Service")
    action_present = "Disable"
    action_past = "Scheduled termination of"
    data_type_singular =_("Service")
    data_type_plural =_("Services")
    classes = ("btn-danger", "btn-terminate")

    def allowed(self, request, datum):
        return bool(len(get_list(request)))

    def action(self, request, bigdata_id):
        delete(request, bigdata_id)


class UpdateRow(tables.Row):
    ajax = True

    def get_data(self, request, bigdata_id):
        return get_service(request, bigdata_id)


def get_bigdata_link(datum):
    view = "horizon:project:bigdata:detail"
    return urlresolvers.reverse(view, args=(datum.id,))


class BigdataTable(tables.DataTable):
    STATUS_CHOICES = (
        ("Create Complete", True),
        ("Create Failed", False),
    )
    SIZE_CHOICES = (
        ("small", "small"),
        ("medium", "medium"),
        ("large", "large"),
    )
    #api_secret = tables.Column("api_secret",
    #                     verbose_name=_("API Secret"),
    #                     link=get_bigdata_link)
    #api_key = tables.Column("api_key",
    #                     verbose_name=_("API Key"),)
    id = tables.Column("id", verbose_name=_("Id"), link=get_bigdata_link)
    status = tables.Column("status",
                         status=True,
                         status_choices=STATUS_CHOICES,
                         filters=(title, replace_underscores),
                         verbose_name=_("Status"),)
    endpoint = tables.Column("endpoint",
                         verbose_name=_("Endpoint"),)

    def get_object_display(self, bigdata):
        return "Your service is enabled"


    class Meta:
        name = "bigdata"
        verbose_name = _("Big Data")
        table_actions = (EnableLink, DisableLink) 
        #status_columns = ["status"]
        row_class = UpdateRow


