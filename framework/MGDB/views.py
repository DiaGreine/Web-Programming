from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import *
# Create your views here.

class HomepageView(ListView):
  template_name = 'home.html'
  context_object_name = 'app'

  def get_queryset(self):
    return App.objects.all()

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(HomepageView, self).get_context_data(**kwargs)
    context['banner_list'] = Banner.objects.all()
    context['rank_list'] = Rank.objects.all()
    return context
