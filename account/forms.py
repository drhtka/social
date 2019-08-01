# -*- coding: utf-8 -*-

from django import forms
from account.models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

class  UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me', 'photo',)


