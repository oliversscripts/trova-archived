from apps.libs import *

# Functions
from apps.functions.sonarr import *

# Models
from apps.models import TvConfig


# Search
@login_required
def TvSearch(request):
    response_data = {}
    return render(request, 'tv.search.html', context=response_data)

@login_required
def TvSearchRequest(request):
    response_data = {}
    tv_config_data = TvConfig.objects.all()[0]
    
    keyword = str(request.GET['search'])

    if request.is_ajax() and keyword:
        search_result = SonarrLookupSeries(keyword)
        if search_result['success']:
            response_data['success'] = True
            response_data['search_results'] = search_result['data']
            shows_result = SonarrGetShows()
            if shows_result['success']:
                response_data['shows_list'] = shows_result['data']

    else:
        response_data['success'] = False

    return JsonResponse(response_data, safe=False)

@login_required
def TvSearchAdd(request):
    response_data = {}
    
    tvdbId = str(request.GET['tvdbId'])
    add_result = SonarrAddSeries(tvdbId)

    return JsonResponse(add_result, safe=False)

@login_required
def TvSearchExists(request):
    response_data = {}
    return JsonResponse(response_data, safe=False)


# Requests
@login_required
def TvRequests(request):
    response_data = {}
    return render(request, 'tv.requests.html', context=response_data)

@login_required
def TvRequestsDetail(request):
    response_data = {}
    return render(request, 'tv.requests.detail.html', context=response_data)


# Schedule
@login_required
def TvSchedule(request):
    response_data = {}

    response_data['sonarr'] = SonarrGetCalendar()
    
    return render(request, 'tv.schedule.html', context=response_data)