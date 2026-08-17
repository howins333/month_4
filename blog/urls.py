"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from posts.views import (
    HelloWorldView, MyNameView, PostListView, PostDetailView, 
    PostCreateView, CategoryCreateView, PostUpdateView, 
    PostDeleteView, PostLikeView
)
from users.views import RegisterView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", HelloWorldView.as_view(), name="hello"),
    path("me/", MyNameView.as_view(), name="me"),
    
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:id>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    
    path("posts/<int:id>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:id>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:id>/like/", PostLikeView.as_view(), name="post_like"),
    
    path('user/register/', RegisterView.as_view(), name="register"),
    path("user/login/", UserLoginView.as_view(), name="login"),
    path("user/logout/", UserLogoutView.as_view(), name="logout")
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)