# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required
#from django.template import Context, loader

from visits.models import Visit

#@login_required
def index(request):
    return render(request, 'visits/index.html')
    #latest_visits = Visit.objects.order_by('-pub_date')[:10]
    #context = {'latest_visits': latest_visits}
    #return render(request, 'visits/index.html', context)

@login_required
def detail(request, visit_id):
    visit = get_object_or_404(Visit, pk=visit_id)
    return render(request, 'visits/detail.html', {'visit': visit})


