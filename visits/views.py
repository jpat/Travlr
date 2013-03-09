# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import Context, RequestContext
from django.core.urlresolvers import reverse

from visits.models import Visit
from visits.forms import VisitForm

#@login_required
def index(request):
    return render(request, 'visits/index.html')

def thanks(request):
    return render(request, 'visits/thanks.html')

def profile(request):
    this_user = request.user
    user_visits = Visit.objects.filter(user = this_user)
    context = {'user': this_user, 'myvisits': user_visits}
    return render(request, 'visits/profile.html', context)

#@login_required
#def visits(request):
    #latest_visits = Visit.objects.order_by('-pub_date')[:10]
    #context = {'latest_visits': latest_visits}
    #return render(request, 'visits/visits.html', context)
    
#@login_required
#def detail(request, visit_id):
    #visit = get_object_or_404(Visit, pk=visit_id)
    #return render(request, 'visits/detail.html', {'visit': visit})

def add_trip(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)

        if form.is_valid():
            visit = form.save(commit=False)
            visit.user = request.user
            visit.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('thanks'))

    else:
        form = VisitForm()
    return render_to_response('visits/add_trip.html', {'form': form}, context_instance=RequestContext(request))


