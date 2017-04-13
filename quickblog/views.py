# Views for the quickblog project

from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Quick Blog!")

