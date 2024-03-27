from django.shortcuts import render
from .models import Produto
from django.views.generic import ListView, DetailView

# Create your views here.

class Index(ListView):
    template_name = "index.html"
    model = Produto
    

class Product(DetailView):
    template_name = "product.html"
    model = Produto