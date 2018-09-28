from django.db import models

class TvConfig(models.Model):

    # General
    enabled = models.BooleanField('Enabled', default=True)
    
    # APIs
    api_key_trakt = models.CharField('Trakt API Key', max_length=254, blank=True)
    api_key_tvdb = models.CharField('TVDB API Key', max_length=254, blank=True)
    
    # Suggestions
    suggestions_trending_enabled = models.BooleanField('Trending Shows', default=True)
    suggestions_popular_enabled = models.BooleanField('Popular Shows', default=True)
    suggestions_anticipated_enabled = models.BooleanField('Anticipated Shows', default=True)

    # Sonarr
    sonnar_host = models.CharField('Sonarr IP or Hostname', max_length=254, blank=True, default='localhost')
    sonnar_port = models.IntegerField('Sonarr Port', blank=True, default=8989)
    sonnar_api_key = models.CharField('Sonarr API Key', max_length=254, blank=True)
    sonarr_sub_directory = models.CharField('Sonarr Sub-directory', max_length=254, blank=True, default='localhost')
    sonarr_ssl = models.BooleanField('Sonarr SSL Enabled', default=False)
    sonarr_quality_profile = models.IntegerField('Sonarr Quality Profile', blank=True, default=1)
    sonarr_tv_dir = models.CharField('Sonarr TV Directory', max_length=254, blank=True)
    sonarr_season_folders = models.BooleanField('Sonarr Season Folders', default=False)

    # Model definitions
    def suggestions_enabled(self):
        "Returns true if any suggestions are enabled"
        if suggestions_trending_enabled or suggestions_popular_enabled or suggestions_anticipated_enabled:
            return True
        else:
            return False
