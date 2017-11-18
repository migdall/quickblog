# Views for the quickblog project

from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render


@csrf_protect
def index(request):
    context = {}
    return render(request, 'index.html', context)
