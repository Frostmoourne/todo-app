from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  middle_name = forms.CharField(max_length=60)

  class Meta:
    model = User
    fields = ('first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', )
