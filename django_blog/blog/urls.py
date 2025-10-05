from django.urls import path
from .views import RegisterView, MyLoginView, MyLogoutView,profile, PostListView, PostCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new', PostCreateView.as_view(), name='create')
]