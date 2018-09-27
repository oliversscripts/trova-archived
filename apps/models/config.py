from django.db import models

class TvConfig(models.Model):
    enabled = models.BooleanField('tv enabled', default=True)
    trakt_api_key = models.CharField(max_length=254, blank=True)
