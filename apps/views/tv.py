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
def TvSchedule(request):
    context = {}
    context['sonarr'] = SonarrGetCalendar()
    
    return render(request, 'tv.schedule.html', context=context)