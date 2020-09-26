from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone
from django.utils.datetime_safe import date

from current_user import get_current_user

class Task(models.Model):
    HIGH = 'ВЫСОКИЙ'
    MEDIUM = "СРЕДНИЙ"
    LOW = 'НИЗКИЙ'
    TO_COMPLETE = "к выполнению"
    IN_PROGRESS = "выполняется"
    COMPLETED = "выполнено"
    CANCELED = 'отменено'

    PRIORITY_CHOICES = (
        (HIGH, 'высокий'),
        (MEDIUM, 'средний'),
        (LOW, 'низкий'),
    )

    STATUS_CHOICES = (
        (TO_COMPLETE, "к выполнению"),
        (IN_PROGRESS, "выполняется"),
        (COMPLETED, "выполнено"),
        (CANCELED, 'отменено')
    )

    title = models.CharField(max_length=140, verbose_name='заголовок')
    text = models.TextField(verbose_name="текст задачи")
    created_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    due_date = models.DateField(null=True, default=timezone.now().strftime("%Y-%m-%d"), verbose_name="Исполнить до",
                                blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Создатель",
        null=True,
        blank=True,
        related_name="todo_created_by",
        on_delete=models.CASCADE,
        default=get_current_user,
    )
    updated = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Исполнитель",
        blank=True,
        null=True,
        related_name="todo_assigned_to",
        on_delete=models.CASCADE,
        default=get_current_user
    )
    priority = models.CharField(verbose_name='приоритет',
                                blank=True,
                                max_length=10,
                                choices=PRIORITY_CHOICES,
                                default=MEDIUM)
    status = models.CharField(verbose_name='статус',
                              choices=STATUS_CHOICES,
                              max_length=20,
                              default=TO_COMPLETE)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

