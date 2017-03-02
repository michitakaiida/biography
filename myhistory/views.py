from django.shortcuts import render
from .models import Profile


def mypage(request):
    #後で、filterはログインIDに変える
    my_prifile = Profile.objects.get(name='michi')

    return render(request, 'myhistory/mypage.html', {'my_prifile': my_prifile})