# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.urls import path, include, re_path
from account import views

#dashboard

urlpatterns = [
    #url(r'^account/', include("account.urls")),

    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    re_path(r'^dashboard/$', views.dashboard, name='dashboard'),
    path('edit/', views.edit_profile, name='edit'),
]
