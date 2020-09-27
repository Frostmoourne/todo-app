from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from datetime import datetime, timedelta
# Create your views here.
from .models import *
from .forms import *


@login_required
def index(request):
    title = 'Задачи'
    user = request.user
    form = TaskForm()
    today = datetime.now().date()
    week = today + timedelta(days=7)
    # Группировка задач по дате выполнения
    if user.groups.filter(name='Руководители').exists():

        users = User.objects.all().order_by('id')
        tasks = Task.objects.all().order_by('-updated')
        if request.GET.get('day') == 'day':
            tasks = Task.objects.filter(Q(due_date__lte=today)).order_by('-updated')
        elif request.GET.get('day') == 'week':
            tasks = Task.objects.filter(Q(due_date__lte=week) & Q(due_date__gt=today)).order_by('-updated')
        elif request.GET.get('day') == 'all':
            tasks = Task.objects.all().order_by('due_date')
        elif request.GET.get('assigned_to'):
            tasks = Task.objects.filter(Q(assigned_to_id=request.GET.get('assigned_to'))).order_by('-updated')
    else:
        tasks = Task.objects.filter(Q(assigned_to=user)).order_by('-updated')
        if request.GET.get('day') == 'day':
            tasks = Task.objects.filter(Q(due_date__lte=today) & Q(assigned_to=user)).order_by('-updated')
        elif request.GET.get('day') == 'week':
            tasks = Task.objects.filter(Q(due_date__lte=week)& Q(due_date__gt=today) & Q(assigned_to=user)).order_by('-updated')
        elif request.GET.get('day') == 'all':
            tasks = Task.objects.filter(Q(assigned_to=user)).order_by('due_date')

    context = {
        'title': title,
        'tasks': tasks,
        'form': form,
        'today': today
    }

    return render(request, 'tasks/index.html', context)


@login_required
def task_add(request):
    user = request.user
    if user.groups.filter(name='Руководители').exists():
        form = TaskForm()
    else:
        form = TaskFormUser()

    if request.method == "POST":
        if user.groups.filter(name='Руководители').exists():
            form = TaskForm(request.POST)
        else:
            form = TaskFormUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'tasks/add_task.html', context)


@login_required
def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    user = request.user

    if user.groups.filter(name='Руководители').exists():
        form = TaskFormEdit(instance=task)
    elif task.created_by == user.username:
        form = TaskFormEdit(instance=task)
    else:
        form = TaskFormEditUser(instance=task)

    if request.method == "POST":
        form = TaskFormEdit(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'tasks/update_task.html', context)


@login_required
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
