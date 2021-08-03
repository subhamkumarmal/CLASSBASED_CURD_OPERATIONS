from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Details

# Create your views here.

class CreateDetails(CreateView):
    model = Details
    fields = ('name','age','email')
    success_url = reverse_lazy('list')

class DetailList(ListView):
    model = Details

class DetailsViews(DetailView):
    model = Details

class DetailsUpdata(UpdateView):
    model=Details
    fields = ('name','age','email')
    success_url = reverse_lazy('list')

class DetailsDelete(DeleteView):
    model = Details
    success_url = reverse_lazy('list')
