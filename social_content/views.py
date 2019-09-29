# -*- coding: utf-8 -*-
from django.views.decorators.http import require_POST
from pyexpat import model

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from social_content.forms import ContentCreateForm, DeleteContentForms
from social_content.models import Content
#instance=request.content,
from my_decorators.decorator_ajax import ajax_required

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

@login_required
def delete_content(request, id, slug):
    new_to_delete = get_object_or_404(Content, id=id, slug=slug)
    if new_to_delete.user !=request.user and not request.user.is_superuser:
        messages.error(request, "Эту запись вы не создавали, не можете удалить.")
        return redirect(new_to_delete.get_absolute_url())

    if request.method == 'POST':
        form = DeleteContentForms(request.POST, instance=new_to_delete)

        if form.is_valid():
            new_to_delete.delete()
            messages.success(request,  'Запись успешно удалена')
            return HttpResponseRedirect('/')

    else:
        form = DeleteContentForms(instance=new_to_delete)
    tempate_vars={'form':form}
    return render(request, 'contents/content/delete.html', tempate_vars)

@login_required
@require_POST
@ajax_required
def content_like(request):
    content_id = request.POST.get('id')
    action = request.POST.get('action')

    if content_id and action:
        try:
            content = Content.objects.get(id=content_id)
            if action == 'like':
                content.users_like.add(request.user)

            else:
                content.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
             pass
    return JsonResponse({'status':'ko'})

