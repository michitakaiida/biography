from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^mypage$', views.mypage, name='mypage'),
    url(r'^event$', views.event_new, name='event_new'),
    url(r'^login/$', auth_views.login, {'template_name': 'myhistory/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'myhistory/logout.html'}, name='logout'),
    #url(r'^', views.mypage, name='mypage'),
]
