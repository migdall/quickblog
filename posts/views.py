from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from .models import Post, PostForm, UploadImagePostForm

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
        return redirect( '/posts/' )

@csrf_exempt
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post:
        if request.method == 'POST':
            new_post_title = request.POST.get('title')
            if request.FILES.get('image'):
                form = UploadImagePostForm(request.POST, request.FILES)
                if form.is_valid():
                    newer_post = form.save()
                    post.title = newer_post.title
                    post.image = newer_post.image
                    post.save()
                    newer_post.delete()
            new_post_description = request.POST.get('description')
            if new_post_title:
                post.title = new_post_title
                post.save()
            if new_post_description:
                post.description = new_post_description
                post.save()
            return redirect( '/posts/' )
        return render(request, 'edit.html', {'post': post})
    return redirect( '/posts/' )

@csrf_exempt
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post:
        post.delete()
    return redirect( '/posts/' )

