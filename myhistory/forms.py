from django import forms
from .models import Event,Timeline

class EventForm(forms.ModelForm):

    turningpoint_flag = forms.BooleanField(label='star')
    turningpoint_flag = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'box1'}))

    class Meta:
        model = Event
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control',"placeholder": "イベント名"}),

        }

        fields = ('event_name', 'event_size','event_date','turningpoint_flag','user','timeline')
