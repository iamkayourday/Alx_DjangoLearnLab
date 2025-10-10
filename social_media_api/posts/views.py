from django.shortcuts import render
from rest_framework import viewsets
from .models import Posts, Comments
from rest_framework.generics import ListAPIView
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

class FeedAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Posts.objects.filter(user__in=followed_users).order_by('-created_at')

