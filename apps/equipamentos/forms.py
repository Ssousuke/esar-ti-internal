from django import forms
from django.forms import ModelForm
from apps.equipamentos.models import Equipments


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
