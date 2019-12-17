from django.shortcuts import render
from django.views.generic import ListView
from .models import App
# Create your views here.

class HomepageView(ListView):
  model = App
  template_name = 'home.html'
