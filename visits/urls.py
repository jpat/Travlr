from django.conf.urls import patterns, url
from django.conf.urls.defaults import *

from django.views.generic import ListView, DetailView
from visits.models import Visit

from visits import views

urlpatterns = patterns('',
    # ex. /visits/
    #url(r'^$', views.visits, name='visits'),
    url(r'^$',
	ListView.as_view(
	    queryset=Visit.objects.order_by('-pub_date'),
	    context_object_name='latest_visits',
	    template_name='visits/visits.html'),
	name='visits'),

    # ex. /visits/5/
    #url(r'^(?P<visit_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/$',
	DetailView.as_view(
	    model=Visit,
	    template_name='visits/detail.html'),
	name='detail'),

    url(r'^add_trip/$', views.add_trip, name='add_trip'),
    

)
