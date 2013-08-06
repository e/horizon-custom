from horizon import workflows, forms, exceptions
from openstack_dashboard.api.base import url_for
from rushstackclient.client import Client as rush_client
from django.utils.translation import ugettext_lazy as _
from .api import create, delete, get_status


class SelectSizeAction(workflows.Action):
    SIZE_CHOICES = (
        ("0", _("Small")),
        ("1", _("Medium")),
        ("2", _("Large")),
    )
    size = forms.ChoiceField(label=_("Size"), choices=SIZE_CHOICES, required=True)

    def handle(self, request, data):
        return True

    class Meta:
        name = _("Select size")
        slug = "select_size"
        help_text = _("Here you can select the size of the Rush Service")


class SelectSize(workflows.Step):
    action_class = SelectSizeAction
    contributes = ("size",)

    class Meta:
        name = _("Size")


class EnableRush(workflows.Workflow):
    slug = "enable_rush"
    name = _("Enable Rush")
    finalize_button_name = _("Enable")
    success_message = _("Preparing your Rush Service...")
    failure_message = _("Unable to launch Rush.")
    success_url = "horizon:project:rushstack:index"
    default_steps = (SelectSize,)

    def handle(self, request, context):
        try:
            create(request, context["size"])
            return True
        except:
            exceptions.handle(request)
            return False


