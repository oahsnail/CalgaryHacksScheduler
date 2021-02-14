# translate model into json
from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'PreferredMaxConsecutiveTime')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'taskName', 'dueDate',
                  'user')


class FixedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedTask
        fields = ('id', 'taskName', 'startTime', 'endTime',
                  'user')
