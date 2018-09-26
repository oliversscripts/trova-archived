from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    plex_id = models.CharField(max_length=254, blank=True)