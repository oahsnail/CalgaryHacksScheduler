from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room, User
from .serializers import RoomSerializer, UserSerializer

# A view function, or view for short, is a Python callable that takes a Web request and returns a Web response.
# This callable is often a function, but can sometimes be a class too


# Create your views here.

def helloWorldView(request):
    return HttpResponse("<h1>Im a stinky poopy bum</h1>")


class CreateRoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListRoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
