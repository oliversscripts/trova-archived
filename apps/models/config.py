from django.db import models

class TvConfig(models.Model):
    enabled = models.BooleanField('TV Enabled', default=True)
    trakt_api_key = models.CharField('Trakt API Key', max_length=254, blank=True)
