from django.db import models
from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry


# TV Options

tv = Section('tv')

@global_preferences_registry.register
class TvEnabled(BooleanPreference):
    section = tv
    name = 'TvEnabled'
    default = True
