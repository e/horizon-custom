from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _
from .api import create
import re


class SelectSizeAction(workflows.Action):
    SIZE_CHOICES = (
        ("1", _("Small")),
        ("2", _("Medium")),
        ("3", _("Large")),
    )
    name = forms.CharField(label=_("Name"), required=True)
    size = forms.ChoiceField(label=_("Size"), choices=SIZE_CHOICES, required=True)

    def clean(self):
        cleaned_data = super(SelectSizeAction, self).clean()
        cleaned_data['name'] = re.sub(' ', '_', cleaned_data['name'])
        return cleaned_data

    def handle(self, request, data):
        return True

    class Meta:
        name = _("Select size")
        slug = "select_size"
        help_text = _("Here you can select the name and size of the Service Directory Service")


class SelectNameAndSize(workflows.Step):
    action_class = SelectSizeAction
    contributes = ("size", "name",)

    class Meta:
        name = _("Name and size")


class EnableServDir(workflows.Workflow):
    slug = "enable_servdir"
    name = _("Enable Service Directory")
    finalize_button_name = _("Enable")
    success_message = _("Preparing your Service Directory Service...")
    failure_message = _("Unable to launch Service Directory.")
    success_url = "horizon:project:servdir:index"
    default_steps = (SelectNameAndSize,)

    def handle(self, request, context):
        try:
            create(request, context["size"], context["name"])
            return True
        except:
            exceptions.handle(request)
            return False


