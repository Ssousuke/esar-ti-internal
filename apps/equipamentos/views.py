from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.equipamentos.models import Equipments
from apps.equipamentos.forms import EquipmentForm


@login_required
def list_equipments(request):
    template_name = 'equipments/equipments.html'
    equipments = Equipments.objects.filter(status=True)
    return render(request, template_name, {'equipments': equipments, 'count_equipment': equipments.count()})


class CreateEquipment(CreateView, LoginRequiredMixin):
    template_name = 'equipments/equipments_form.html'
    model = Equipments
    form_class = EquipmentForm
    success_url = reverse_lazy('equipments:list')


class EditEquipment(UpdateView, LoginRequiredMixin):
    template_name = 'equipments/equipments_form.html'
    model = Equipments
    form_class = EquipmentForm
    success_url = reverse_lazy('equipments:list')


@login_required
def delete_equipment(request, pk):
    equipment = Equipments.objects.get(pk=pk)
    equipment.delete()
    return redirect('equipments:list')
