from django.urls import path
from .views import *
urlpatterns = [
    path('', helloWorldView),
    path('createroom', CreateRoomView.as_view()),
    path('listrooms', ListRoomView.as_view()),
    path('usertest', ListUserView.as_view())
]
