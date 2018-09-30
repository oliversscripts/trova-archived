from apps.includes import *

from apps.models import TvConfig

class TvConfigForm(ModelForm):
    class Meta:
        model = TvConfig
        fields = '__all__'
        
