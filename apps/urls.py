from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    path('apps/', views.Home, name='home'),
    path('tv_search/', views.TvSearch, name='tv_search'),
]