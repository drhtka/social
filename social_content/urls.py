# -*- coding: utf-8 -*-
from django.conf.urls import url
from social_content import views
from django.urls import path, re_path
#app_name = 'social_content'
app_name = "images"

urlpatterns = [
    re_path(r'^create/$', views.content_create, name='create'),
    re_path(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.content_detail, name='detail'),
    re_path(r'^detail/(?P<id>\d+)/(?P<slug>[-\w]+)/edit/$', views.content_edit, name='iii'),
]



