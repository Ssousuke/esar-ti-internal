from django import forms
from django.forms import ModelForm
from apps.equipamentos.models import TypeEquipment, Equipments


class TypeEquipmentForm(ModelForm):
    class Meta:
        model = TypeEquipment
        fields = '__all__'
        # widgets


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipments
        fields = '__all__'
        # widgets
