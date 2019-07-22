# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

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
    return render(request, 'contents/content/create.html', {'form':form}) # где форму показать, вернуть на какой странице эт овсе проделать

#display the record
def content_detail(request, id, slug):
    content_detail = get_object_or_404(Content, id=id, slug=slug)
    return render(request,
        "contents/content/detail.html",
        {'content_detail':content_detail}
    )
