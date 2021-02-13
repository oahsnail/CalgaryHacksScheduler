from django.urls import path
from .views import *
urlpatterns = [
    path('', helloWorldView),
    path('createroom', CreateRoomView.as_view()),
    path('listrooms', ListRoomViews.as_view()),
    path('deleterooms', DeleteRoomViews.as_view())
]
