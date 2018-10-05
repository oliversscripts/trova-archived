from apps.libs import *

# Functions
from apps.functions.sonarr import *

# Models
from apps.models import TvConfig
from apps.models import TvRequest


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
    sonarr_data = jsonpickle.decode(add_result['data'])
    current_user = request.user
    new_request = TvRequest(
        requested_by = current_user, 
        sonarr_id = sonarr_data['id'],
        title = sonarr_data['title']
    )
    try:
        new_request.save()
        messages.success(request, 'Request Added')
    except:
        messages.error(request, 'Failed to Add Request')

    return HttpResponseRedirect(reverse('apps:tv.requests.detail', args = (new_request.request_id,)))


@login_required
def TvSearchExists(request):
    response_data = {}
    return JsonResponse(response_data, safe=False)



# Requests
@login_required
def TvRequestsAll(request):
    response_data = {}

    tv_config_data = TvConfig.objects.all()[0]

    try:
        requests = TvRequest.objects.all()
        response_data['requests_data'] = jsonpickle.encode(requests, unpicklable=False)
        response_data['success'] = True
    except:
        response_data['success'] = False

    try:
        sonarr_result = SonarrGetShows()
        if sonarr_result['success']:
            response_data['sonarr_data'] = sonarr_result['data']
    except:
        response_data['sonarr_data'] = ''

    response_data['requests_persona'] = 'all'
    response_data['sonarr_url'] = SonarrGetUrl()
    response_data['tv_config_data'] = jsonpickle.encode(tv_config_data, unpicklable=False)

    return render(request, 'tv.requests.html', context=response_data)


@login_required
def TvRequestsUser(request):
    response_data = {}

    current_user = request.user
    tv_config_data = TvConfig.objects.all()[0]

    try:
        requests_data = TvRequest.objects.all()
        requests_data_filtered = requests_data.filter(requested_by=current_user)
        response_data['requests_data'] = jsonpickle.encode(requests_data, unpicklable=False)
        response_data['success'] = True
    except:
        response_data['success'] = False

    try:
        sonarr_result = SonarrGetShows()
        if sonarr_result['success']:
            response_data['sonarr_data'] = sonarr_result['data']
    except:
        response_data['sonarr_data'] = ''

    response_data['requests_persona'] = 'user'
    response_data['sonarr_url'] = SonarrGetUrl()
    response_data['tv_config_data'] = jsonpickle.encode(tv_config_data, unpicklable=False)

    return render(request, 'tv.requests.html', context=response_data)


@login_required
def TvRequestsDetail(request, request_id):
    response_data = {}
    tv_request_data = TvRequest.objects.get(request_id=request_id)
    
    try:
        sonarr_json = SonarrGetShow(tv_request_data.sonarr_id)
        sonarr_data = jsonpickle.decode(sonarr_json['data'])
    except:
        sonarr_data = 'Request removed from Sonarr'

    if sonarr_json['success']:
        try:
            show_json = SonarrLookupSeries("tvdb:" + str(sonarr_data['tvdbId']))
            show_data = jsonpickle.decode(show_json['data'])
        except:
            show_data = 'Problem with Sonarr'
    else:
        show_data = ''
    
    response_data['tv_request_data'] = tv_request_data
    response_data['show_data'] = show_data
    response_data['sonarr_data'] = sonarr_data

    return render(request, 'tv.requests.detail.html', context=response_data)

@login_required
def TvRequestsDelete(request, request_id):
    response_data = {}

    current_user = request.user
    
    tv_request_data = TvRequest.objects.get(request_id=request_id)
    if tv_request_data.requested_by == current_user:
        try:
            TvRequest.objects.filter(request_id=request_id).delete()
            response_data['success'] = True
            messages.success(request, 'Request Deleted')
        except:
            response_data['success'] = False
            messages.error(request, 'Delete Failed')
    else:
        response_data['success'] = False
        messages.warning(request, 'Permission Denied')
    
    return HttpResponseRedirect(reverse('apps:tv.requests.user'))



# Schedule
@login_required
def TvSchedule(request):
    response_data = {}

    response_data['sonarr'] = SonarrGetCalendar()
    
    return render(request, 'tv.schedule.html', context=response_data)