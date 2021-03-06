# Generated by Django 3.1.1 on 2020-09-24 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('created_date', models.DateField(default='2020-09-24')),
                ('due_date', models.DateField(default='2020-09-24')),
                ('completed', models.BooleanField(default=False)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('HIGH', 'высокий'), ('MEDIUM', 'средний'), ('LOW', 'низкий')], default='MEDIUM', max_length=10, verbose_name='приоритет')),
                ('status', models.CharField(choices=[('TO COMPLETE', 'к выполнению'), ('IN PROGRESS', 'выполняется'), ('COMPLETE', 'выполнена'), ('CANCELED', 'отменена')], default='TO COMPLETE', max_length=20, verbose_name='статус')),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_assigned_to', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todo_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
