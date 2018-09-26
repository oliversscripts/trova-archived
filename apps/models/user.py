from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    plex_id = models.TextField(max_length=500, blank=True)