from apps.libs import *

# Models
from apps.models import TvConfig

def SonarrGetUrl():
    tv_config_data = TvConfig.objects.all()[0]
    
    url = ''
    if (tv_config_data.sonarr_ssl):
        url += 'https://'
    else:
        url += 'http://'
    url += tv_config_data.sonarr_host
    url += ':'
    url += str(tv_config_data.sonarr_port)
    if tv_config_data.sonarr_sub_directory:
        url += v_config_data.sonarr_sub_directory
    url += '/api'
    
    return url

def SonarrGetApiKey():
    tv_config_data = TvConfig.objects.all()[0]
    return  tv_config_data.sonarr_api_key

def SonarrGetStatus():
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try:
        sonarrData['data'] = json.dumps(snr.get_system_status())
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData

def SonarrGetCalendar():
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try:
        sonarrData['data'] = json.dumps(snr.get_calendar())
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData


def SonarrGetCalendarRange(start_date,end_date):
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())
    
    try:
        sonarrData['data'] = json.dumps(snr.get_calendar_range(start_date,end_date))
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData