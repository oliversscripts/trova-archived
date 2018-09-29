from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    path('apps/', views.Home, name='home'),
    path('configure_tv/', views.ConfigureTv, name='configure_tv'),
    path('tv_schedule/', views.TvSchedule, name='tv_schedule'),
    path('tv_search/', views.TvSearch, name='tv_search'),
    
    
]