from apps.libs import *

from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    path('apps/', views.Home, name='home'),
    path('config/tv/', views.ConfigTv, name='config.tv'),
    path('config/tv/test/sonarr/', views.ConfigTvTestSonarr, name='config.tv.test.sonarr'),
    path('tv/schedule/', views.TvSchedule, name='tv.schedule'),
    path('tv/search/', views.TvSearch, name='tv.search'),
    path('tv/search/request/', views.TvSearchRequest, name='tv.search.request'),

]