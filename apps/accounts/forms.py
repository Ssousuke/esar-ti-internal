from django.forms import ModelForm
from django import forms
from apps.accounts.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
