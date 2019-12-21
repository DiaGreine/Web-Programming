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


class SearchpageView(ListView):
  template_name = 'search.html'
  model = Category
  context_object_name = 'categorires'

  def get_queryset(self):
    return Category.objects.all()


class SearchResultView(ListView):
  template_name = 'search_result.html'
  context_object_name = 'search_result'

  def get_queryset(self):  # new
    name = self.request.GET.get('search')
    category = self.request.GET.get('category')
    object_list = App.objects.filter(name__contains=name).filter(category__name__contains=category)

    return object_list


class AppDetailView(ListView):
  template_name = 'app_details.html'
  model = App

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(AppDetailView, self).get_context_data(**kwargs)
    context['detail'] = App.objects.filter(name__exact=self.kwargs['name'])
    context['related'] = App.objects.filter(category__name__contains=self.kwargs['category']) \
      .exclude(name__exact=self.kwargs['name'])
    return context


class RankView(ListView):
  template_name = 'rankings.html'
  model = MatchTable
  context_object_name = 'table'

  def get_queryset(self):
    return MatchTable.objects.filter(name__name__exact='Top Games')


class CategoryView(ListView):
  template_name = 'category.html'
  context_object_name = 'app'

  def get_queryset(self):
    return App.objects.all()

  def get_context_data(self, *, object_list=None, **kwargs):
    context = super(CategoryView, self).get_context_data(**kwargs)
    context['categories'] = Category.objects.all()
    return context


