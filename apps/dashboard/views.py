from django.shortcuts import render
from apps.equipamentos.models import Equipments
from apps.rede.models import Networks


def dashboard(request):
    equipment_count = Equipments.objects.all().count()
    equipment_network_count = Networks.objects.all().count()
    context = {'equipment_count': equipment_count,
               'equipment_network_count': equipment_network_count}
    return render(request, 'dashboard/dashboard.html', context)
