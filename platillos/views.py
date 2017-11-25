from django.shortcuts import render
from .models import Platillo
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class PlatilloListView(ListView):
    model = Platillo

class PlatilloDetailView(DetailView):
    model = Platillo

class PlatilloCreateView(CreateView):
    model = Platillo
    fields = '__all__'

class PlatilloDeleteView(DeleteView):
    model = Platillo
    success_url = reverse_lazy('platillos:list')

class PlatilloUpdateView(UpdateView):
    model = Platillo
    fields = '__all__'