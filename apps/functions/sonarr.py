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

def SonarrGetShows():
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try:
        sonarrData['data'] = json.dumps(snr.get_series())
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData

def SonarrGetShow(sonarr_id):
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try:
        sonarrData['data'] = json.dumps(snr.get_series_by_series_id(sonarr_id))
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData

def SonarrLookupSeries(search_words):
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try:
        sonarrData['data'] = json.dumps(snr.lookup_series(search_words))
        sonarrData['success'] = True
    except:
        sonarrData['success'] = False

    return sonarrData

def SonarrAddSeries(tvdbId):
    show_json = {}
    sonarrData = {}
    tv_config_data = TvConfig.objects.all()[0]

    snr = SonarrAPI(SonarrGetUrl(), SonarrGetApiKey())

    try: 
        show_json['data'] = snr.construct_series_json(
            tvdbId,
            tv_config_data.sonarr_quality_profile,
            tv_config_data.sonarr_season_folders, 
            tv_config_data.sonarr_monitored, 
            tv_config_data.sonarr_search_missing, 
        )
        show_json['success'] = True
    except: 
        show_json['success'] = False

    if show_json['success']:
        try:
            sonarrData['data'] = json.dumps(snr.add_series(show_json['data']))
            sonarrData['success'] = True
        except:
            sonarrData['success'] = False
    else:
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

def SonarrGetImage(image_type, sonarr_id):    
    url = SonarrGetUrl()
    url += '/MediaCover/' + sonarr_id + '/' + image_type + '.jpg'

    headers = {
        'X-Api-Key': SonarrGetApiKey()
    }
    image_response = requests(url, headers=headers, timeout=3)

    return HttpResponse(image_response, content_type="image/jpeg")