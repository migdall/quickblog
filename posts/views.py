from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect( '/posts/login/' )

@csrf_exempt
def index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html', {})
    return redirect( '/posts/login/' )

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_active:
            auth.login( request, user )
            return redirect( '/posts/' )

    return render(request, 'login.html', {})

