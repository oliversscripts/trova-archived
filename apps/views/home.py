from apps.includes import *

@login_required
def Index(request):
    return HttpResponseRedirect(reverse('apps:home'))

@login_required
def Home(request):
    context = {}
    return render(request, 'home.default.html', context=context)


