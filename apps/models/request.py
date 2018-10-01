from apps.libs import *

class TvRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class MovieRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class MusicRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class BookRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
