from apps.includes import *

# Models
from apps.models import TvConfig

@login_required
def TvSearch(request):
    context = {}
    return render(request, 'tv.search.html', context=context)

@login_required
def TvSchedule(request):
    context = {}

    tv_config_data = TvConfig.objects.all()[0]
 
    url = 'http://' + tv_config_data.sonarr_host + ':' + str(tv_config_data.sonarr_port) + '/api/calendar?apikey=' + tv_config_data.sonarr_api_key
    
    try:
        r = requests.get(url, params=request.GET)
        context['success'] = True
        context['schedule'] = json.dumps(r.text)

    except requests.exceptions.Timeout:
        context['success'] = False
        context['errorMsg'] = 'Timeout'

    except requests.exceptions.TooManyRedirects:
        context['success'] = False
        context['errorMsg'] = 'Too Many Redirects'

    except requests.exceptions.RequestException as e:
        context['success'] = False
        context['errorMsg'] = e
    

    return render(request, 'tv.schedule.html', context=context)