from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Posts, Comments
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    # Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    #  Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
