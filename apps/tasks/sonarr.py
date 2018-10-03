from apps.libs import *

# Functions
from apps.functions.sonarr import *

# Models
from apps.models import TvRequest

@background(queue='sonarr')
def SonarrUpdateRequests(user_id):
    reponse_data = {}
    requests_list = TvRequest.objects.all()
    sonarr_response = SonarrGetShows()
    shows_list = jsonpickle.decode(sonarr_response)

    return reponse_data

    