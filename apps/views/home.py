from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {}
    return render(request, 'base.default.html', context=context)

def test_template(request):
    context = {}
    return render(request, 'base.generic.html', context=context)

