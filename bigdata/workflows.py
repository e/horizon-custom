from horizon import workflows, forms, exceptions
from django.utils.translation import ugettext_lazy as _
from .api import create, get_keypair_list
import re


class SelectKeypairAction(workflows.Action):
    # name = forms.CharField(label=_("Name"), required=True)

    keypair = forms.ChoiceField(label=_("Keypair"), required=True)

    def clean(self):
        cleaned_data = super(SelectKeypairAction, self).clean()
        # cleaned_data['name'] = re.sub(' ', '_', cleaned_data['name'])
        return cleaned_data

    def handle(self, request, data):
        return True

    def populate_keypair_choices(self, request, context):
        try:
            keypairs = get_keypair_list(request)
            keypair_list = [(kp.name, kp.name) for kp in keypairs]
        except Exception:
            keypair_list = []
            exceptions.handle(request, _('Unable to retrieve keypairs.'))
        if keypair_list:
            if len(keypair_list) == 1:
                self.fields['keypair'].initial = keypair_list[0][0]
            keypair_list.insert(0, ("", _("Select a keypair")))
        else:
            keypair_list = (("", _("No keypairs available.")),)
        return keypair_list

    class Meta:
        name = _("Select Keypair")
        slug = "select_keypair"
        help_text = _("Here you can select the keypair for the Big Data Service")


class SelectKeypair(workflows.Step):
    action_class = SelectKeypairAction
    contributes = ("keypair",)

    class Meta:
        name = _("Keypair")


class EnableBigdata(workflows.Workflow):
    slug = "enable_bigdata"
    name = _("Enable Big Data Profile Service")
    finalize_button_name = _("Enable")
    success_message = _("Preparing your Big Data Profile Service...")
    failure_message = _("Unable to launch Big Data.")
    success_url = "horizon:project:bigdata:index"
    default_steps = (SelectKeypair,)

    def handle(self, request, context):
        try:
            create(request, context["keypair"])
            return True
        except:
            exceptions.handle(request)
            return False


