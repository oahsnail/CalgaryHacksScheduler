from django.urls import path
from .views import *
urlpatterns = [
    path('', helloWorldView),
    path('createroom', CreateRoomView.as_view()),
    path('createuser', CreateUserView.as_view()),
    path('listrooms', ListRoomView.as_view()),
    path('listusers', ListUserView.as_view()),
    path('listtasks', ListTaskView.as_view())
]
