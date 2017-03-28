from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm
from django.contrib.auth import authenticate, login
import pdb;


def mypage(request):
    # 後で、filterはログインIDに変える
    #pdb.set_trace()
    my_prifile = Profile.objects.get(user=request.user)
    my_timeline_list = Timeline.objects.filter(user=request.user)
    my_event_list = Event.objects.filter(user=request.user).order_by('event_date')

    print(my_event_list)
    return render(request, 'myhistory/mypage.html', {'my_prifile': my_prifile,
                                                     'my_timeline_list':my_timeline_list,
                                                     'my_event_list':my_event_list})
def event_new(request):

    if request.method == "POST":
        form = EventForm(request.POST)
        #pdb.set_trace()
        if form.is_valid():
            post = form.save(commit=False)
            form.profile_id = request.user
            post.save()
            return render(request, 'myhistory/mypage.html')
    else:
        form = EventForm()
    return render(request, 'myhistory/event_edit.html', {'form': form})
