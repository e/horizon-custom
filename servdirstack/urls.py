from django.conf.urls.defaults import patterns, url

from .views import IndexView, LaunchServDirStackView


urlpatterns = patterns('openstack_dashboard.dashboards.project.servdirstack.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^enable$', LaunchServDirStackView.as_view(), name='enable'),
)
