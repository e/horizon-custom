tdaf-ost-horizonx
=================

Openstack panels for TDAF Services

For each panel, a subdirectory should be created to keep
organized this repo.


Installation
------------

To deploy this panels in a working horizon installation, some of the original
horizon files must be overwritten with the files inside horizon-custom, and
there must be a symbolic link for each of the panel directories inside
horizon's "project" directory. The name of the link must be in accordance with
the contents of horizon-custom/dashboard.py.

    cp horizon-custom/dashboard.py $HORIZON/openstack_dashboard/dashboards/project/dashboard.py
    cp horizon-custom/logo.png $HORIZON/openstack_dashboard/static/dashboard/img/logo.png
    cp horizon-custom/logo-splash.png $HORIZON/openstack_dashboard/static/dashboard/img/logo-splash.png
    cp horizon-custom/favicon.ico $HORIZON/openstack_dashboard/static/dashboard/img/favicon.ico
    ln -s rushstack $HORIZON/openstack_dashboard/dashboards/project/httprelayer
    ln -s servdirstack $HORIZON/openstack_dashboard/dashboards/project/servdirstack

Another installation method would be to create a new Django project, add
horizon as well as all the custom panels to INSTALLED_APPS, and add a
customization module to your settings.HORIZON_CONFIG:

    HORIZON_CONFIG = {
            "customization_module": "my_project.overrides"
    }

You can do essentially anything you like in the customization module. For
example, you could change the name of a panel:

    from django.utils.translation import ugettext_lazy as _

    import horizon

    # Rename "User Settings" to "TDAF User Options"
    settings = horizon.get_dashboard("settings")
    user_panel = settings.get_panel("user")
    user_panel.name = _("TDAF User Options")

