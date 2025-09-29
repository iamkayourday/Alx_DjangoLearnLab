from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PostForm, CustomUserCreationForm, ProfileForm
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Register.html'
    success_url = '/login/'

    def form_valid(self, form):
        self.object = form.save() 
        login(self.request, self.object)
        return redirect(self.get_success_url())
    
class MyLoginView(LoginView):
    template_name = 'Login.html'
    redirect_authenticated_user = True


class MyLogoutView(LogoutView):
    next_page = '/login/'
    template_name = 'Logout.html'
