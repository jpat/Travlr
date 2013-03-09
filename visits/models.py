from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

#class Country(models.Model):
	#country = CountryField(unique=True)


class Visit(models.Model):
	user = models.ForeignKey(User)
	country = models.ForeignKey('Country')
	#countries = models.ManyToManyField(CountryField)
	visitDate = models.DateField('date of trip')
	pub_date = models.DateTimeField('date published', auto_now = True)

class Country(models.Model):
	name = models.CharField(max_length = 256)
	code = models.CharField(max_length = 8)
