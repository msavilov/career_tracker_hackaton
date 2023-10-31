from django.contrib import admin

from .models import (Candidate, Contact, Course, Employment, Experience,
                     Location, Portfolio, WorkFormat,)

admin.site.register(Candidate)
admin.site.register(Contact)
admin.site.register(Course)
admin.site.register(Employment)
admin.site.register(Experience)
admin.site.register(Location)
admin.site.register(Portfolio)
admin.site.register(WorkFormat)
