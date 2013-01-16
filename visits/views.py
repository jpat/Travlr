# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader

from visits.models import Visit

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
    #latest_trips = Visit.objects.order_by('-pub_date')[:10]
    #template = loader.get_template('visits/index.html')
    #context = Context({
#	'latest_trips': latest_trips,
    #})
   # return HttpResponse(template.render(context))

def detail(request, visit_id):
    return HttpResponse("You're looking at visit %s." % visit_id)
