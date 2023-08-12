from django.contrib import admin
from .models import CharityOrg, Family, Individual, Subscriber, Event, HumanitarianContainer

admin.site.register(CharityOrg)
admin.site.register(Individual)
admin.site.register(Family)
admin.site.register(Subscriber)
admin.site.register(Event)
admin.site.register(HumanitarianContainer)
# Register your models here.











