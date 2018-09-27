from django.forms import ModelForm, modelformset_factory
from apps.models import TvConfig

class TvConfigForm(ModelForm):
    class Meta:
        model = TvConfig
        fields = '__all__'