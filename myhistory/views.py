from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
import pdb;


@login_required(login_url='login')
def mypage(request):
    my_prifile = Profile.objects.get(user=request.user)
    my_timeline_list = Timeline.objects.filter(user=request.user)
    my_event_list = Event.objects.filter(user=request.user).order_by('event_date')

    return render(request, 'myhistory/mypage.html', {'my_prifile': my_prifile,
                                                     'my_timeline_list':my_timeline_list,
                                                     'my_event_list':my_event_list})


@login_required(login_url='login')
def profile(request):
    my_prifile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=my_prifile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=my_prifile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            if profile.profile_image is None or profile.profile_image == "":
                profile.profile_image = 'images/default_image.jpg'
            profile.save()
            return redirect(mypage)

    return render(request, 'myhistory/edit_profile.html', {'form': form})


def event_new(request,timeline_name):

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.timeline = Timeline.objects.get(timeline_name=timeline_name, user=request.user)
            event.save()
            return redirect(mypage)
    else:
        form = EventForm()

    return render(request, 'myhistory/event_new.html', {'form': form})
