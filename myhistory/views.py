from django.shortcuts import render
from .models import Profile, Event, Timeline
from .forms import EventForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
import pdb;


@login_required(login_url='login')
def mypage(request):
    # 後で、filterはログインIDに変える
    #pdb.set_trace()
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
        print(form)
        #pdb.set_trace()
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            if profile.profile_image is None or profile.profile_image == "":
                profile.profile_image = 'images/default_image.jpg'
            profile.save()

            return redirect(mypage)

    return render(request, 'myhistory/edit_profile.html', {'form': form})

def event_new(request):

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            form.profile_id = request.user
            post.save()
            return render(request, 'myhistory/mypage.html')
    else:
        form = EventForm()
    return render(request, 'myhistory/event_edit.html', {'form': form})
