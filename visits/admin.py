from django.contrib import admin
from visits.models import Visit

class VisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'country_names')

admin.site.register(Visit, VisitAdmin)
