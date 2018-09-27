from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

@login_required
def ConfigureTv(request):
    context = {}
    return render(request, 'config.tv.html', context=context)