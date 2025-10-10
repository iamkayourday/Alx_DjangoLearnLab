from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user_id = kwargs.get('user_id')
        try:
            target_user = CustomUser.objects.get(id=target_user_id)
            request.user.following.add(target_user)
            return Response({'detail': f'You are now following {target_user.username}.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user_id = kwargs.get('user_id')
        try:
            target_user = CustomUser.objects.get(id=target_user_id)
            request.user.following.remove(target_user)
            return Response({'detail': f'You have unfollowed {target_user.username}.'}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

