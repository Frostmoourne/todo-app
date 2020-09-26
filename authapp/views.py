from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import *


def registration_view(request):

    # (предотвращаем заход по прямой ссылке)
    # если авторизован, то
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('account'))

    form = SignUpForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()

        new_user.groups.add(Group.objects.get(name='Пользователи'))

        return redirect('/')

    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authapp/signup.html', context)

