from django.urls import path

from . import views
from .models import *

urlpatterns = [
  path('', views.HomepageView.as_view(), name='home'),
  path('search/', views.SearchpageView.as_view(), name='search'),
  path('search_result/', views.SearchResultView.as_view(), name='search_result'),
  path('app_detail/<str:name>/<str:category>', views.AppDetailView.as_view(), name='app_detail'),
  path('ranking/', views.RankView.as_view(), name='ranking'),
  path('category/', views.CategoryView.as_view(), name='category'),
]
