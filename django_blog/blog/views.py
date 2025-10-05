from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import PostForm, CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = '/login/'

    def form_valid(self, form):
        self.object = form.save() 
        login(self.request, self.object)
        return redirect(self.get_success_url())
    
class MyLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=request.user)
    posts = Post.objects.filter(author=request.user).order_by('-published_date')  
    return render(request, "blog/profile.html", {"form": form, "posts": posts})


class MyLogoutView(LogoutView):
    next_page = '/login/'
    template_name = 'Logout.html'


# Creating Blog Post Management Features
# List Post
class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

# Create Post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Post Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Post Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    template_name = 'blog/post_confirm_delete.html'
    context_object_name = 'posts'
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author