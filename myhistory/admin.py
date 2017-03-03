from django.contrib import admin

# Register your models here.
from .models import Profile, Event, EventType

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(EventType)