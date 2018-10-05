from apps.libs import *

class TvRequest(models.Model):
    request_id = models.AutoField('Request Id', primary_key=True)
    sonarr_id = models.IntegerField(unique=True, db_index=True, blank=False)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Show Name', max_length=254, blank=True)
    
class MovieRequest(models.Model):
    request_id = models.AutoField('Request Id', primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class MusicRequest(models.Model):
    request_id = models.AutoField('Request Id', primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class BookRequest(models.Model):
    request_id = models.AutoField('Request Id', primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
