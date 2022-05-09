from django import forms
from django.forms import ModelForm
from apps.rede.models import Networks


class NetworkForm(ModelForm):
    class Meta:
        model = Networks
        fields = '__all__'
        # widgets
