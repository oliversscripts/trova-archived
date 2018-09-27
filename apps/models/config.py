from django.db import models

class TvConfig(models.Model):
    enabled = models.BooleanField('TV Enabled', default=True)
    
    api_key_trakt = models.CharField('Trakt API Key', max_length=254, blank=True)
    api_key_tvdb = models.CharField('TVDB API Key', max_length=254, blank=True)

    suggestions_trending_enabled = models.BooleanField('Trending Shows', default=True)
    suggestions_popular_enabled = models.BooleanField('Popular Shows', default=True)
    suggestions_anticipated_enabled = models.BooleanField('Anticipated Shows', default=True)

    def suggestions_enabled(self):
        "Returns true if any suggestions are enabled"
        if suggestions_trending_enabled or suggestions_popular_enabled or suggestions_anticipated_enabled:
            return True
        else:
            return False
