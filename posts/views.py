from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from posts.models import Post
# Create your views here.

def Hello_World(request: HttpRequest):
    return HttpResponse("<1>Hello World!<1>")

def my_name(request: HttpRequest):
    return HttpResponse("<1>Azis<1>")

def post_list(request: HttpRequest):
    posts = Post.objects.filter(is_active=True)
    
    return render(request, "posts.html", {"posts": posts})