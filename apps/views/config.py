from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

from apps.models import TvConfig
from apps.forms import TvConfigForm

@login_required
def ConfigureTv(request):
    context = {}
    message = {}

    if request.method == 'POST':
        tv_config_data = TvConfig.objects.all()[0]
        tv_config_form = TvConfigForm(request.POST, instance=tv_config_data)
        tv_config_form.save()
        message = {'type':'success', 'text':'Saved'}
        
    else:
        if TvConfig.objects.all().exists():
            tv_config_data = TvConfig.objects.all()[0]
        else:
            tv_config_data = TvConfig.objects.create()

        tv_config_form = TvConfigForm(instance=tv_config_data)


    context['form'] = tv_config_form
    context['message'] = message

    return render(request, 'config.tv.html', context=context)

