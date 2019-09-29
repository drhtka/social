# -*- coding: utf-8 -*-
from django.contrib import admin
from account.models import Profile #Contact

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']

#class ContactAdmin(admin.ModelAdmin):
#    list_display = ['user_from', 'user_to']

admin.site.register(Profile, ProfileAdmin)
#admin.site.register(Contact, ContactAdmin)