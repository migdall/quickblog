from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from .models import Post, PostForm

# Create your views here.

@csrf_exempt
def logout(request):
    auth.logout(request)
    return redirect( '/posts/login/' )

@csrf_exempt
def index(request):
    if request.user.is_authenticated():
        posts_list = Post.objects.all()
        return render(request, 'index.html', {'posts': posts_list})
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

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user.person
            post.save()
            return redirect( '/posts/' )

