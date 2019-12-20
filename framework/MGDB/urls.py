from django.urls import path

from . import views

urlpatterns = [
  path('', views.HomepageView.as_view(), name='home'),
  path('search/', views.SearchpageView.as_view(), name='search'),
  path('search_result/', views.SearchResultView.as_view(), name='search_result')
]