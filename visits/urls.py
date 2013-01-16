from django.conf.urls import patterns, url

from visits import views

urlpatterns = patterns('',
    # ex /views/
    url(r'^$', views.index, name='index')
    # /views/5/
   # url(r'^(?P<visit_id>\d+)/$', views.detail, name='detail'),
)
