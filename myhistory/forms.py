from django import forms
from .models import Event, Profile, Timeline
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EventForm(forms.ModelForm):
#    turningpoint_flag = forms.BooleanField()

    class Meta:
        model = Event
        fields = ('event_name', 'event_size', 'event_date', 'turningpoint_flag')


class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('mission_statement', 'birthday','dream1','dream2','dream3','strongPoint1','strongPoint2','strongPoint3',
                  'weekPoint1','weekPoint1','weekPoint2','weekPoint3','profile_image')


class TimelineForm(forms.ModelForm):

    class Meta:
        model = Timeline
        fields = ('timeline_name',)


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1","password2","first_name", "last_name")

#class EventForm(forms.ModelForm):
#    turningpoint_flag = forms.BooleanField(label='star')
#    turningpoint_flag = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id': 'box1'}))
#
#    class Meta:
#        model = Event
#        widgets = {
#            'event_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "イベント名"}),
#
#        }
#
#        fields = ('event_name', 'event_size', 'event_date', 'turningpoint_flag', 'user', 'timeline')