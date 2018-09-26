from django.urls import path
from . import views

app_name = 'apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('test_template', views.test_template, name='test_template')
]