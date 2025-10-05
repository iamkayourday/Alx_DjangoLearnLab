from django.urls import path
from .views import RegisterView, MyLoginView, MyLogoutView,profile, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('post/<int:pk>/update/', PostDeleteView.as_view(), name='update'),

]