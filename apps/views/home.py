from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

@login_required
def Index(request):
    return HttpResponseRedirect(reverse('apps:home'))

@login_required
def Home(request):
    context = {}
    return render(request, 'home.default.html', context=context)


