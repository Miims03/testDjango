from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [(AllowAny)]

    def get_queryset(self):
        return User.objects.all()
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)