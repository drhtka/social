# -*- coding: utf-8 -*-
from django.conf.urls import url
from social_content import views

app_name = 'social_content'

urlpatterns = [
    url(r'^create/$', views.content_create, name='create'),
    #url(r'^detali/(?<id>\d+)/(?P<slug>)[-\w]+/$', views.content_detali, name='detali'),
]



