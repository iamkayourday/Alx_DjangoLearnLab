from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts, Comments
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    # Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    #  Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
