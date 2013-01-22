from django.db import models
from django.contrib.auth.models import User
from django_countries import CountryField
from django.forms import ModelForm

# Create your models here.

class Visit(models.Model):
	user = models.ForeignKey(User)
	country = CountryField()
	visitDate = models.DateField('date of trip')
	pub_date = models.DateTimeField('date published', auto_now = True)

