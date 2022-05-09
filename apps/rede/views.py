from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.rede.forms import NetworkForm

from apps.rede.models import Networks


def network_list(request):
    template_name = 'networks/networks.html'
    networks = Networks.objects.all()
    return render(request, template_name, {'networks': networks})


class CreateNetwork(CreateView):
    template_name = 'networks/network_form.html'
    model = Networks
    form_class = NetworkForm
    success_url = reverse_lazy('network:list')


class UpdateNetNetwork(UpdateView):
    template_name = 'networks/network_form.html'
    model = Networks
    form_class = NetworkForm
    success_url = reverse_lazy('network:list')


def delete_network(request, pk):
    network = Networks.objects.get(pk=pk)
    network.delete()
    return redirect('network:list')
