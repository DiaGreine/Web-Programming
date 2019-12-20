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
    context['collection'] = MatchTable.objects.all()
    context['editor_pick'] = EditorPick.objects.all()
    return context

class SearchpageView(TemplateView):
  template_name = 'search.html'

class SearchResultView(ListView):
  template_name ='search_result.html'
  context_object_name = 'search_result'

  def get_queryset(self):  # new
    name = self.request.GET.get('search')
    category = self.request.GET.get('category')
    object_list = App.objects.filter(name__contains=name).filter(category__name__contains=category)

    return object_list
