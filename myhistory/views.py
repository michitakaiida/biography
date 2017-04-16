from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm, ProfileForm, TimelineForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
import pdb;


@login_required(login_url='login')
def mypage(request):
    try:
        my_prifile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        form = ProfileForm()
        return render(request, 'myhistory/edit_profile.html', {'form': form})

    my_timeline_list = Timeline.objects.filter(user=request.user)
    my_event_list = Event.objects.filter(user=request.user).order_by('event_date')

    return render(request, 'myhistory/mypage.html', {'my_prifile': my_prifile,
                                                     'my_timeline_list': my_timeline_list,
                                                     'my_event_list': my_event_list})


@login_required(login_url='login')
def profile(request):
    my_prifile = Profile()
    #my_prifile = get_object_or_404(Profile, user=request.user)
    try:
        my_prifile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=my_prifile)
    except Profile.DoesNotExist:
        form = ProfileForm()

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
    TimelineFormSet = modelformset_factory(model=Timeline, form=TimelineForm, extra=0,
                                           can_delete=True, can_order=True)
    formset = TimelineFormSet(request.POST)

    if request.method == "POST":
        formset = TimelineFormSet(request.POST)

        if formset.is_valid():

            for form in formset:
                f = form.save(commit=False)
                f.user = request.user
                f.save()

            for obj in formset.deleted_forms:
                Timeline.objects.get(id = obj['id'].value()).delete()

            return redirect(mypage)
    else:
        formset = TimelineFormSet(queryset=Timeline.objects.filter(user=request.user))

    return render(request, 'myhistory/timeline_edit.html', {'formset': formset})


@login_required(login_url='login')
def event_new(request, timeline_name):
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


def sign_up(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'myhistory/signup.html', {'form': form})
