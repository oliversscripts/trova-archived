from apps.libs import *

from . import views

app_name = 'apps'
urlpatterns = [
    url(r'^$', views.Index, name='index'),
    path('apps/', views.Home, name='home'),
    
    path('config/tv/', views.ConfigTv, name='config.tv'),
    path('config/tv/test/sonarr/', views.ConfigTvTestSonarr, name='config.tv.test.sonarr'),

    path('tv/schedule/', views.TvSchedule, name='tv.schedule'),
    path('tv/schedule/range/', views.TvScheduleRange, name='tv.schedule.range'),
    
    path('tv/search/', views.TvSearch, name='tv.search'),
    path('tv/search/request/', views.TvSearchRequest, name='tv.search.request'),
    path('tv/search/add/', views.TvSearchAdd, name='tv.search.add'),
    path('tv/search/exists/', views.TvSearchExists, name='tv.search.exists'),

    path('tv/requests/', views.TvRequests, name='tv.requests'),
    path('tv/requests/<int:request_id>/', views.TvRequestsDetail, name='tv.requests.detail'),
    path('tv/requests/<int:request_id>/delete/', views.TvRequestsDelete, name='tv.requests.delete'),
]