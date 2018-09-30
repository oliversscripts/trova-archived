from apps.includes import *

class TvConfig(models.Model):
    # General
    tv_enabled = models.BooleanField('Enabled', default=True)

    # APIs
    api_key_trakt = models.CharField('Trakt API Key', max_length=254, blank=True)
    api_key_tvdb = models.CharField('TVDB API Key', max_length=254, blank=True)
    
    # Suggestions
    suggestions_trending_enabled = models.BooleanField('Trending Shows', default=True)
    suggestions_popular_enabled = models.BooleanField('Popular Shows', default=True)
    suggestions_anticipated_enabled = models.BooleanField('Anticipated Shows', default=True)

    # Sonarr
    sonarr_host = models.CharField('Sonarr IP or Hostname', max_length=254, blank=True, default='localhost')
    sonarr_port = models.IntegerField('Sonarr Port', blank=True, null=True, default='8989')
    sonarr_api_key = models.CharField('Sonarr API Key', max_length=254, blank=True)
    sonarr_sub_directory = models.CharField('Sonarr URL Path', max_length=254, blank=True)
    sonarr_ssl = models.BooleanField('Sonarr SSL Enabled', default=False)
    sonarr_quality_profile = models.IntegerField('Sonarr Quality Profile', blank=True, null=True)
    sonarr_tv_dir = models.CharField('Sonarr TV Folder Root', max_length=254, blank=True)
    sonarr_season_folders = models.BooleanField('Sonarr Season Folders', default=False)

    # Model definitions
    def tv_suggestions_enabled(self):
        "Returns true if any suggestions are enabled"
        if self.suggestions_trending_enabled or self.suggestions_popular_enabled or self.suggestions_anticipated_enabled:
            return True
        else:
            return False
