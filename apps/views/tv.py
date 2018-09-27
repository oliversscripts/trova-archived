from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse


@login_required
def TvSearch(request):
    context = {}
    return render(request, 'tv.search.html', context=context)