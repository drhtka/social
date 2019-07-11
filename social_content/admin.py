# -*- coding: utf-8 -*-
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from social_content.models import Content

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('entry',)

admin.site.register(Content, NewsAdmin)