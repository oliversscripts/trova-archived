from apps.libs import *

# Functions
from apps.functions.sonarr import *

# Models
from apps.models import TvConfig

@login_required
def TvSearch(request):
    context = {}
    return render(request, 'tv.search.html', context=context)

@login_required
def TvSearchRequest(request):
    reponse_data = {}
    tv_config_data = TvConfig.objects.all()[0]
    
    keyword = str(request.GET['search'])
    language = 'en'
    if request.is_ajax():
        if tv_config_data.api_key_tvdb != "":
            db = tvdbApi.TVDB(tv_config_data.api_key_tvdb, ignore_case=True)
            result = db.search(keyword, language)
            json_result = jsonpickle.encode(result, unpicklable=False, max_depth=5)
            response_data = {
                'success': True,
                'response': json_result
            }
        else:
            response_data = {
                'success':False,
                'response':'TVDB Api Key Missing'
            }

        #return JsonResponse(response_data)

@login_required
def TvSearchRequestNew(request):
    response_data = {}
    tv_config_data = TvConfig.objects.all()[0]
    
    keyword = str(request.GET['search'])

    if request.is_ajax() and keyword:
        search_result = SonarrLookupSeries(keyword)
        if search_result['success']:
            response_data['success'] = True
            response_data['search_results'] = jsonpickle.encode(search_result['data'], unpicklable=False)
            shows_result = SonarrGetShows()
            if shows_result['success']:
                response_data['shows_list'] = jsonpickle.encode(shows_result['data'], unpicklable=False)

    else:
        response_data['success'] = False

    return JsonResponse(response_data, safe=False)

    

@login_required
def TvSchedule(request):
    context = {}
    context['sonarr'] = SonarrGetCalendar()
    
    return render(request, 'tv.schedule.html', context=context)