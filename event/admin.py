from django.contrib import admin
from event.models import Event, EventType, SubEventType, Spot, City

admin.site.register(Event)
admin.site.register(EventType)
admin.site.register(SubEventType)
admin.site.register(Spot)
admin.site.register(City)