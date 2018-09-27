from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('tv_search/', views.tv_search, name='tv_search'),
]