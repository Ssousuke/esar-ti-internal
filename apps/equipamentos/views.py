from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.equipamentos.models import Equipments, TypeEquipment
from apps.equipamentos.forms import EquipmentForm, TypeEquipmentForm


def list_equipments(request):
    template_name = 'equipments/equipments.html'
    equipments = Equipments.objects.filter(status=True)
    return render(request, template_name, {'equipments': equipments})


class CreateEquipment(CreateView):
    template_name = 'equipments/equipments_form.html'
    model = Equipments
    form_class = EquipmentForm
    success_url = reverse_lazy('equipments:list')


class EditEquipment(UpdateView):
    template_name = 'equipments/equipments_form.html'
    model = TypeEquipment
    form_class = TypeEquipmentForm
    success_url = reverse_lazy('equipments:list')


def delete_equipment(request, pk):
    equipment = Equipments.objects.get(pk=pk)
    equipment.delete()
    return redirect('equipments:list')
