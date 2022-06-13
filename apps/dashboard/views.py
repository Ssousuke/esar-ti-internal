from django.shortcuts import render
from apps.rede.models import Networks


def dashboard(request):
    equipment_network_count = Networks.objects.all().count()
    context = {'equipment_network_count': equipment_network_count}
    return render(request, 'dashboard/dashboard.html', context)
