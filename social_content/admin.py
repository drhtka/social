# -*- coding: utf-8 -*-
from django.contrib import admin
from social_content.models import Content
from django_summernote.admin import SummernoteModelAdmin

# from .models import *

class ContentAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('entry',)

admin.site.register(Content, ContentAdmin,)
