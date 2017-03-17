from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm

def mypage(request):
    # 後で、filterはログインIDに変える
    my_prifile = Profile.objects.get(name='michi')
    my_timeline_list = Timeline.objects.filter(profile=my_prifile)
    my_event_list = Event.objects.filter(profile=my_prifile).order_by('event_date')

    print(my_event_list)
    return render(request, 'myhistory/mypage.html', {'my_prifile': my_prifile,
                                                     'my_timeline_list':my_timeline_list,
                                                     'my_event_list':my_event_list})
def event_new(request):
    form = EventForm()
    return render(request, 'myhistory/event_edit.html', {'form': form})