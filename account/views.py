# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from account.forms import LoginForm
# Create your views here.


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
    return render(request, "account/dashboard.html", {'username': auth.get_user(request).username}) #  будет отображать вошел пользователь или не вошел




