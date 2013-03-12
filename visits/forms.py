from django import forms
from django.forms import ModelForm
from django.forms import extras
from visits.models import *

class VisitForm(ModelForm):
	visitDate = forms.DateField(
	    widget=extras.SelectDateWidget(years=range(2013,1950,-1)), label="Date of Visit")
	class Meta:
	    model = Visit
	    exclude = ('user',)
	    widgets = {
	    	'countries': forms.SelectMultiple(attrs={'size': 10})
	    }
	    help_text = ""
