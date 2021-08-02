from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Details

# Create your views here.

class CreateDetails(CreateView):
    model = Details
    fields = ('name','age','email')

class DetailList(ListView):
    model = Details

class DetailsViews(DetailView):
    model = Details

class DetailsUpdata(UpdateView):
    model=Details
    fields = ('name','age','email')

class DetailsDelete(DetailsViews):
    model = Details