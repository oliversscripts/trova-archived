from apps.libs import *

class User(AbstractUser):
    plex_id = models.CharField(max_length=254, blank=True)
    manager = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.username)
    
    def is_admin(self):
        return self.admin
    
    def is_manager(self):
        return self.manager