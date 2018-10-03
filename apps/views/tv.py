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
def TvSearchAdd(request):
    response_data = {}
    return JsonResponse(response_data, safe=False)

@login_required
def TvSearchExists(request):
    response_data = {}
    return JsonResponse(response_data, safe=False)

@login_required
def TvSchedule(request):
    context = {}
    context['sonarr'] = SonarrGetCalendar()
    
    return render(request, 'tv.schedule.html', context=context)