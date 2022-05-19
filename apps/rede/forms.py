from django import forms
from django.forms import ModelForm
from apps.rede.models import Networks


class NetworkForm(ModelForm):
    class Meta:
        model = Networks
        fields = '__all__'
        widgets = {
            'department': forms.TextInput(
                attrs={
                    'class': 'form-control m-1'
                }
            ),
            'equipment': forms.Select(
                attrs={
                    'class': 'form-control m-1'
                }
            ),
            'ipv4_or_ipv6': forms.TextInput(
                attrs={
                    'class': 'form-control m-1'
                }
            ),
        }
