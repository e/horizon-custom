from django.conf.urls.defaults import patterns, url

from .views import IndexView, LaunchAccountsView, DetailView


urlpatterns = patterns('openstack_dashboard.dashboards.project.identity.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^enable$', LaunchAccountsView.as_view(), name='enable'),
    url(r'^(?P<instance_id>[^/]+)/$', DetailView.as_view(), name='detail'),
)
