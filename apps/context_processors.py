from apps.models import TvConfig

def get_configuration_options(request):
    all_config_data = {}

    if TvConfig.objects.all().exists():
        all_config_data['tv_config'] = TvConfig.objects.all()[0]

    return {
        'all_config_data': all_config_data,
    }
