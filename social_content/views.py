# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from social_content.forms import ContentCreateForm
from social_content.models import Content

@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.user = request.user
            new_content.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm()# показать форму
    return render(request, 'contents/content/cteate.html', {'form':form}) # где форму показать, вернуть на какой странице эт овсе проделать


