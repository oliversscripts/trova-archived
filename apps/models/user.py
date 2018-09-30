from apps.includes import *

class User(AbstractUser):
    plex_id = models.CharField(max_length=254, blank=True)
    trova_admin = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.username)