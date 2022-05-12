from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.rede.forms import NetworkForm

from apps.rede.models import Networks


@login_required
def network_list(request):
    template_name = 'networks/networks.html'
    networks = Networks.objects.all()
    return render(request, template_name, {'networks': networks})


class CreateNetwork(CreateView, LoginRequiredMixin):
    template_name = 'networks/network_form.html'
    model = Networks
    form_class = NetworkForm
    success_url = reverse_lazy('network:list')

    def form_valid(self, form):
        form.save()
        return super(CreateNetwork, self).form_valid(form)


class UpdateNetNetwork(UpdateView, LoginRequiredMixin):
    template_name = 'networks/network_form.html'
    model = Networks
    form_class = NetworkForm
    success_url = reverse_lazy('network:list')

    def form_valid(self, form):
        form.save()
        return super(UpdateNetNetwork, self).form_valid(form)


@login_required
def delete_network(request, pk):
    network = Networks.objects.get(pk=pk)
    network.delete()
    return redirect('network:list')
