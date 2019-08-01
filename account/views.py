# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from account.forms import LoginForm
from account.forms import UserEditForm, ProfileEditForm

from account.models import Profile


def user_login(request):
    if request.method == 'POST': #  не будет виден в строке браузера
        form = LoginForm(request.POST)  # request.POST создст штмл форму из Django создаст как мы прописали в forms
        if form.is_valid(): #  проверка правильно заполнен пароль
            cd = form.cleaned_data  # метод cleaned_data создаем формы и проверяем
            user = authenticate(username=cd['username'], password=cd['password'])  # это словарь ключем является поле из forms

            if user is not None: # говоря проще если пользователь существует
                if user.is_active:
                    login(request, user)
                    return redirect ('dashboard') # перенаправить в кабинет
                    #return redirect('/') # вернуть на главную

                else: # если пароль и имя не подошли
                    return HttpResponse('Disabled account')

            else: # если вообще все пошло не так
                return HttpResponse('Invalid login and password')

    else:
        form = LoginForm()
    return render(request, "account/login.html", {'form': form, 'username': auth.get_user(request).username}) #  будет отображать вошел пользователь или не вошел

def user_logout(request):
    auth.logout(request)# используем библиотеку auth
    return redirect('/')# куда нас вернуть после того как мы вышли, на главную

@login_required#чтобы могли входить только авторизовааннрые пользователи
def dashboard(request):
    context = RequestContext(request)
    to = User.objects.get(username=request.user)
    try:
        profile = Profile.objects.get(user=to)
    except ObjectDoesNotExist:
        profile=None
    return render(request, "account/dashboard.html", {'username': auth.get_user(request).username, #  будет отображать вошел пользователь или не вошел
                                                      'to':to,
                                                      'profile':profile,
                                                      'user':request.user.get_full_name,
                                                      'last_name':request.user.last_name,
                                                      'first_name':request.user.first_name,
                                                      'ip_address':request.META['REMOTE_ADDR']
                                                      })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)

        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно обнавлен!.')
            return redirect('dashboard')
        else:
            messages.error(request,'Ой! Ошибка при обновлении профиля. Попробуйте снова.')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request,
        "account/edit.html",
        {'user_form':user_form,
         'profile_form':profile_form}
    )

