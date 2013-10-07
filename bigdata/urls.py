from django.conf.urls.defaults import patterns, url

from .views import IndexView, LaunchBigdataView, DetailView


urlpatterns = patterns('openstack_dashboard.dashboards.project.bigdata.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^enable$', LaunchBigdataView.as_view(), name='enable'),
    url(r'^(?P<instance_id>[^/]+)/$', DetailView.as_view(), name='detail'),
)
