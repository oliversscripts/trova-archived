from django.contrib import admin

from .models import User
from .models import TvConfig

admin.site.register(User)

admin.site.register(TvConfig)