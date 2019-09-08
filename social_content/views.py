# -*- coding: utf-8 -*-
from pyexpat import model

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from social_content.forms import ContentCreateForm
from social_content.models import Content
#instance=request.content,

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
        form = ContentCreateForm(request.POST, request.FILES)# показать форму
    return render(request, 'contents/content/create.html', {'form':form}) # где форму показать, вернуть на какой странице это все проделать
"""

@login_required
def content_create(request):
    new_content = get_object_or_404(Content, id=id, slug=slug)
    if new_content.user == request.user and not request.user.is_superuser:
        pass

    if request.method == 'POST':
        form = ContentCreateForm(instance=new_content, data=request.POST, files=request.FILES)

        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.user = request.user
            new_content.save()
            return redirect(new_content.get_absolute_url())
    else:# показать форму
        form = ContentCreateForm(instance=new_content)
    context = {'form':form, 'create':False}
    return render(request, 'contents/content/create.html', context) # где форму показать, вернуть на какой странице эт овсе проделать

"""
#display the record
def content_detail(request, id, slug):
    content_detail = get_object_or_404(Content, id=id, slug=slug)
    return render(request,
        "contents/content/detail.html",
        {'content_detail':content_detail}
    )

@login_required
def content_edit(request, id, slug):
    new_content = get_object_or_404(Content, id=id, slug=slug)
    if new_content.user == request.user and not request.user.is_superuser:
        pass

    if request.method == 'POST':
        form = ContentCreateForm(instance=new_content, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(new_content.get_absolute_url())
    else:
        form = ContentCreateForm(instance=new_content)
    context = {'form':form, 'create':False}
    return render(request, 'contents/content/create.html', context)
