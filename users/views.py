from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout
from users.forms import UserForm, LoginForm

# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    form = UserForm()
    if request.method.lower() == "post":
        form = UserForm(request.POST)

        if form.is_valid():
            form.instance.set_password(form.cleaned_data["password"])
            form.instance.save()
            login(request, form.instance)

            return redirect("post_list")

    return render(request, "users/register.html", {"form": form})


def login_view(request: HttpRequest) -> HttpResponse:
    form = UserForm()

    if request.method.lower() == "post":
        form = LoginForm()

        if form.isvalid():
            user = get_object_or_404(User, username=form.cleaned_data["username"])

            if user.check_password(form.cleaned_data["password"]):
                login(request, user)
                return redirect("post_list")
            

    return render(request, "users/login.html", context={"form": form})


def logout_view(request: HttpRequest) -> HttpResponse:
    if request.method.lower() == 'post':
        logout(request)

        return redirect("post_list")

    
