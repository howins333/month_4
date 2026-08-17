from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from posts.models import Post, Category
from posts.forms import PostForm, CategoryForm

class HelloWorldView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Hello World!</h1>")

class MyNameView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Azis</h1>")

class PostListView(ListView):
    model = Post
    template_name = "posts/posts.html"
    context_object_name = "posts"
    ordering = ["-created_ad"]

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = 'id'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create_post.html"
    success_url = reverse_lazy("post_list")
    login_url = "login"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "posts/create_category.html"
    success_url = reverse_lazy("post_create")
    login_url = "login"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/update_post.html"
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse("post_detail", kwargs={"id": self.object.id})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
    pk_url_kwarg = 'id'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostLikeView(LoginRequiredMixin, View):
    login_url = "login"

    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        next_url = request.POST.get('next', reverse('post_detail', args=[id]))
        return redirect(next_url)