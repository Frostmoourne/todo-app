from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('task_edit/<int:pk>/', views.task_edit, name="edit"),
    path('delete/<int:pk>/', views.task_delete, name="delete"),
    path('add/', views.task_add, name="add"),

]