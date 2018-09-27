from django.db import models
import dbsettings

class ConfigTv(dbsettings.Group):
    enabled = dbsettings.BooleanValue('is tv enabled')
    trakt_api_key = dbsettings.StringValue('trakt api key')