from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm, ProfileForm, TimelineForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
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
    my_prifile = get_object_or_404(Profile, user=request.user)
    #my_prifile = Profile.objects.get(user=request.user)
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


@login_required(login_url='login')
def timeline_new(request):

    if request.method == "POST":
        form = TimelineForm(request.POST)
        if form.is_valid():
            timeline = form.save(commit=False)
            timeline.user = request.user
            timeline.save()
            return redirect(mypage)
    else:
        form = TimelineForm()

    return render(request, 'myhistory/timeline_new.html', {'form': form})


@login_required()
def timeline_edit(request):


    TimelineFormSet = modelformset_factory(model=Timeline, form=TimelineForm,extra=0, can_delete=True)
    formset = TimelineFormSet(request.POST)

    if request.method == "POST":
        formset = TimelineFormSet(request.POST)

        if 1==1 or TimelineFormSet.is_valid():
            formset.save()
            for form in formset:
                f = form.save(commit=False)
                f.user = request.user
                f.save()

            return redirect(mypage)
    else:
        formset = TimelineFormSet(queryset=Timeline.objects.filter(user=request.user))

    return render(request, 'myhistory/timeline_edit.html', {'formset': formset})


@login_required(login_url='login')
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
