# forms.py
from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


# Post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'avatar', ]


# POST FORM
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        