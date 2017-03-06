from django.contrib import admin

# Register your models here.
from .models import Profile, Event, Timeline

admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(Timeline)