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
    tv_requests_data = TvRequest.objects.all()
    
    keyword = str(request.GET['search'])

    if request.is_ajax() and keyword:
        search_result = SonarrLookupSeries(keyword)
        if search_result['success']:
            response_data['success'] = True

            response_data['search_results'] = search_result['data']
            response_data['tv_config_data'] = jsonpickle.encode(tv_config_data, unpicklable=False)
            response_data['requests_data'] = jsonpickle.encode(tv_requests_data, unpicklable=False)
            response_data['sonarr_url'] = SonarrGetUrl()

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
    
    sonarr_id = str(request.GET['sonarr_id'])

    try:
        sonarr_json = SonarrGetShow(sonarr_id)
        sonarr_data = jsonpickle.decode(sonarr_json['data'])
    except:
        sonarr_data = 'Problem Adding Show to Requests'
    
    if sonarr_json['success']:
        current_user = request.user
        new_request = TvRequest(
            requested_by = current_user, 
            sonarr_id = sonarr_data['id'],
            title = sonarr_data['title']
        )
    try:
        new_request.save()
        messages.success(request, 'Request Added')
        response_data['success'] = True
    except:
        messages.error(request, 'Failed to Add Request')
        response_data['success'] = False

    return HttpResponseRedirect(reverse('apps:tv.requests.detail', args = (new_request.request_id,)))


# Requests
@login_required
def TvRequests(request):
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

    response_data['sonarr_url'] = SonarrGetUrl()
    response_data['tv_config_data'] = jsonpickle.encode(tv_config_data, unpicklable=False)

    return render(request, 'tv.requests.html', context=response_data)


@login_required
def TvRequestsDetail(request, request_id):
    response_data = {}

    tv_config_data = TvConfig.objects.all()[0]
    tv_config_json = jsonpickle.encode(tv_config_data, unpicklable=False)

    tv_request_data = TvRequest.objects.get(request_id=request_id)
    tv_request_json = jsonpickle.encode(tv_request_data, unpicklable=False)

    response_data['tv_config_data'] = tv_config_data
    response_data['tv_config_json'] = tv_config_json

    response_data['tv_request_data'] = tv_request_data
    response_data['tv_request_json'] = tv_request_json

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
    
    return render(request, 'tv.schedule.html', context=response_data)


@login_required
def TvScheduleRange(request):
    tv_config_data = TvConfig.objects.all()[0]
    sonarr_tz = timezone(tv_config_data.sonarr_timezone)

    start_date = request.GET.get('start', '')
    end_date = request.GET.get('end', '')

    response_data = SonarrGetCalendarRange(start_date,end_date)
    calender_data = jsonpickle.decode(response_data['data'])

    event_data = []
    for event_item in calender_data:
        start_local = datetime.strptime(event_item['airDate'] + " " + event_item['series']['airTime'], "%Y-%m-%d %H:%M")
        start_with_tz = sonarr_tz.localize(start_local, is_dst=None)

        end_local = start_local + timedelta(minutes=int(event_item['series']['runtime']))
        end_with_tz = sonarr_tz.localize(end_local, is_dst=None)

        event = {}
        event['title'] = event_item['series']['title']
        event['start'] = start_with_tz
        event['end'] = end_with_tz
        event['allDay'] = False
        event['url'] = ''
        event_data.append(event)
    
    return JsonResponse(event_data, safe=False)