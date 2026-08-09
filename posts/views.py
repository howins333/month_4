from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from posts.models import Post
from posts.forms import PostForm, CategoryForm

def Hello_World(request: HttpRequest):
    return HttpResponse("<h1>Hello World!</h1>")

def my_name(request: HttpRequest):
    return HttpResponse("<h1>Azis</h1>")

def post_list(request: HttpRequest):
    posts = Post.objects.order_by("-created_ad").all()
    return render(request, "posts/posts.html", {"posts": posts})

def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=id)
    return render(request, "posts/post_detail.html", {"post": post})

def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect("post_list")
    else:
        form = PostForm()
        
    return render(request, "posts/create_post.html", {"form": form})

def create_category(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_create")
    else:
        form = CategoryForm()
        
    return render(request, "posts/create_category.html", {"form": form})