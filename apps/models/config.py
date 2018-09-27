from django.db import models

class TvConfig(models.Model):
    enabled = models.BooleanField('TV Enabled', default=True)
    
    api_key_trakt = models.CharField('Trakt API Key', max_length=254, blank=True)
    api_key_tvdb = models.CharField('TVDB API Key', max_length=254, blank=True)

    suggestions_enabled = models.BooleanField('Suggestions Enabled', default=True)
    suggestions_trending_enabled = models.BooleanField('Trending Shows Enabled', default=True)
    suggestions_popular_enabled = models.BooleanField('Popular Shows Enabled', default=True)
    suggestions_anticipated_enabled = models.BooleanField('Anticipated Shows Enabled', default=True)
