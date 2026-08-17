from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth import login
from users.forms import UserForm

class RegisterView(CreateView):
    form_class = UserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("post_list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = "users/login.html"
    next_page = reverse_lazy("post_list")
    redirect_authenticated_user = True 

class UserLogoutView(LogoutView):
    next_page = reverse_lazy("post_list")