from django import forms
from django.forms import ModelForm, DateInput, TextInput


from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status', 'created_by', 'updated']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class TaskFormUser(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['status', 'created_by', 'assigned_to', 'updated']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class TaskFormEdit(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['created_by', 'updated']

        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }


class TaskFormEditUser(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['due_date', 'created_by', 'priority', 'created_date', 'assigned_to', 'updated']

        # widgets = {
        #     'due_date': DateInput(attrs={'type': 'date'})
        # }

    def __init__(self, *args, **kwargs):
        super(TaskFormEditUser, self).__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['title'].widget.attrs['readonly'] = True
            self.fields['text'].widget.attrs['readonly'] = True



