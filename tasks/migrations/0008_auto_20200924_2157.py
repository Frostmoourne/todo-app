# Generated by Django 3.1.1 on 2020-09-24 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0007_auto_20200924_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2020-09-24', null=True, verbose_name='Исполнить до'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('ВЫСОКИЙ', 'высокий'), ('СРЕДНИЙ', 'средний'), ('НИЗКИЙ', 'низкий')], default='СРЕДНИЙ', max_length=10, verbose_name='приоритет'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('к выполнению', 'к выполнению'), ('выполняется', 'выполняется'), ('выполнена', 'выполнена'), ('отменена', 'отменена')], default='к выполнению', max_length=20, verbose_name='статус'),
        ),
    ]