from django.conf.urls.defaults import patterns, url

from .views import IndexView, LaunchRushstackView


urlpatterns = patterns('openstack_dashboard.dashboards.project.rushstack.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^enable$', LaunchRushstackView.as_view(), name='enable'),
)
