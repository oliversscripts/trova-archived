from apps.includes import *

# Forms
from apps.forms import TvConfigForm

# Models
from apps.models import TvConfig




@login_required
def ConfigTv(request):
    context = {}

    if request.method == 'POST':
        tv_config_data = TvConfig.objects.all()[0]
        tv_config_form = TvConfigForm(request.POST, instance=tv_config_data)
        
        if tv_config_form.is_valid():
            tv_config_form.save()
            messages.success(request, 'TV Config Saved')
        else:
            messages.error(request, 'Problem saving TV Config')
        
    else:
        if TvConfig.objects.all().exists():
            tv_config_data = TvConfig.objects.all()[0]
            tv_config_form = TvConfigForm(instance=tv_config_data)
        else:
            tv_config_data = TvConfig(tv_enabled=True)
            tv_config_data.save()
            tv_config_form = TvConfigForm(instance=tv_config_data)

    context['form'] = tv_config_form

    return render(request, 'config.tv.html', context=context)

@login_required
def ConfigTvTestSonarr(request):
    context = {}

    tv_config_data = TvConfig.objects.all()[0]

    url = 'http://' + tv_config_data.sonarr_host + ':' + str(tv_config_data.sonarr_port) + '/api/calendar?apikey=' + tv_config_data.sonarr_api_key
    r = requests.get(url, params=request.GET)
    
    schedule_dict = json.dumps(r.text)
    
    scheduleData = []

    context['schedule'] = json.dumps(r.text)

    return render(request, 'config.tv.test.sonarr.html', context=context)


