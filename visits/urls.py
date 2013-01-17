from django.conf.urls import patterns, url
from django.conf.urls.defaults import *

from visits import views

urlpatterns = patterns('',
    # ex. /visits/
    url(r'^$', views.index, name='index'),
    # ex. /visits/5/
    url(r'^(?P<visit_id>\d+)/$', views.detail, name='detail'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
)
