from django.conf.urls.defaults import patterns, url

from .views import IndexView, LaunchRushstackView, DetailView


urlpatterns = patterns('openstack_dashboard.dashboards.project.httprelayer.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^enable$', LaunchRushstackView.as_view(), name='enable'),
    url(r'^(?P<instance_id>[^/]+)/$', DetailView.as_view(), name='detail'),
)
