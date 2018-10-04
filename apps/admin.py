from django.contrib import admin

from .models import User

from .models import TvConfig
from .models import TvRequest

admin.site.register(User)

admin.site.register(TvConfig)
admin.site.register(TvRequest)