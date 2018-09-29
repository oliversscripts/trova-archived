from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.shortcuts import render
from django.urls import reverse

import json
import requests

from apps.models import TvConfig

@login_required
def TvSearch(request):
    context = {}
    return render(request, 'tv.search.html', context=context)

@login_required
def TvSchedule(request):
    tv_config_data = TvConfig.objects.all()[0]
    
    url = 'http://' + tv_config_data.sonarr_host + ':' + str(tv_config_data.sonarr_port) + '/api/calendar?apikey=' + tv_config_data.sonarr_api_key
    r = requests.get(url, params=request.GET)
    
    schedule_dict = json.dumps(r.text)
    
    scheduleData = []

    # for episode in schedule_dict:
    #     episodeData = {}
    #     episodeData['title'] = episode.title
    #     scheduleData.append(episodeData)
    
    context = {
        'schedule': json.dumps(r.text)
    }
    return render(request, 'tv.schedule.html', context=context)