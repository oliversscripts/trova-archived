from django.db import models
import dbsettings

class TvOptions(dbsettings.Group):
    enabled = dbsettings.BooleanValue('is tv functionality enabled', default=True)
    trakt_api_key = dbsettings.StringValue()
