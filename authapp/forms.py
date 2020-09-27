from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
  middle_name = forms.CharField(max_length=60)

  class Meta:
    model = User
    fields = ('first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', )

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    self.fields['middle_name'].widget.attrs.update({'class': 'form-control'})
    self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    self.fields['username'].widget.attrs.update({'class': 'form-control'})
    self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control'})
