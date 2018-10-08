from apps.libs import *

class TvConfig(models.Model):
    # General
    tv_enabled = models.BooleanField('Enabled', default=True)

    # APIs
    api_key_trakt_client_id = models.CharField('Trakt API Client ID', max_length=254, blank=True)
    api_key_trakt_client_secret = models.CharField('Trakt API Client Secret', max_length=254, blank=True)
    
    # Suggestions
    suggestions_trending_enabled = models.BooleanField('Trending Shows', default=True)
    suggestions_popular_enabled = models.BooleanField('Popular Shows', default=True)
    suggestions_anticipated_enabled = models.BooleanField('Anticipated Shows', default=True)

    # Sonarr
    sonarr_host = models.CharField('IP or Hostname', max_length=254, blank=True, default='localhost')
    sonarr_port = models.IntegerField('Port', blank=True, null=True, default='8989')
    sonarr_api_key = models.CharField('API Key', max_length=254, blank=True)
    sonarr_sub_directory = models.CharField('URL Path', max_length=254, blank=True)
    sonarr_ssl = models.BooleanField('SSL Enabled', default=False)
    sonarr_quality_profile = models.IntegerField('Quality Profile', blank=True, null=True)
    sonarr_tv_dir = models.CharField('TV Media Root', max_length=254, blank=True)
    sonarr_season_folders = models.BooleanField('Season Folders', default=False)
    sonarr_monitored = models.BooleanField('Show Monitored', default=False)
    sonarr_search_missing = models.BooleanField('Search Missing', default=False)
    sonarr_timezone = models.CharField('Timezone Sonarr is Hosted', max_length=254, blank=True)

    # Model definitions
    def tv_suggestions_enabled(self):
        "Returns true if any suggestions are enabled"
        if self.suggestions_trending_enabled or self.suggestions_popular_enabled or self.suggestions_anticipated_enabled:
            return True
        else:
            return False
