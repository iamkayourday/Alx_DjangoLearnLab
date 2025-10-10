from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts, Comments
from rest_framework.generics import ListAPIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    # Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    #  Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        # ["Post.objects.filter(author__in=following_users).order_by"
        return Posts.objects.filter(user__in=followed_users).order_by('-created_at')

