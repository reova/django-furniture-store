from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # creating a form with user data

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # check if the user is in the db

            if user:
                auth.login(request, user)  # if the user is in the db - authorize

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Авторизация',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            user = form.instance  # get data from form
            auth.login(request, user)  # authorize user

            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Кабинет',
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)

    return redirect(reverse('main:index'))
