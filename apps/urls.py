from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    path('apps/', views.Home, name='home'),
    path('config_tv/', views.ConfigTv, name='config_tv'),
    path('tv_search/', views.TvSearch, name='tv_search'),
    
]