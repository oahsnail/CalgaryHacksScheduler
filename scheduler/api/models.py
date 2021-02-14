import random
import string
import datetime
from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
# a model is basicaly a sql table, but django specific abstraction
# see this page for some sql/models side by sides: https://docs.djangoproject.com/en/3.1/topics/db/models/
# Also, here are all the info about fields and field types in django: https://docs.djangoproject.com/en/3.1/ref/models/fields/

# here we're basically specifying a Room model/db table that contains the info and some rules about that room.

# basic rule: fat models, and thin views.


# test model, not a actual one we use

def deleteTask(id):
    Task.objects.filter(id=id).delete()


def deleteUser(id):
    User.objects.filter(id=id).delete()


def deleteFixedTask(id):
    FixedTask.objects.filter(id=id).delete()


# returned user would have id: user.id by default
# can get things like password by just calling user.password
def createNewUser(username, password, PreferredMaxConsecutiveTime):
    user = User.objects.create(
        username=username, password=password, PreferredMaxConsecutiveTime=PreferredMaxConsecutiveTime)
    print(type(user))

    return user


def createNewTask(taskName, dueDate, user):

    task = Task(taskName=taskName, dueDate=dueDate, user=user)
    task.save(force_insert=True)

    return task


def createNewFixedTask(taskName, startTime, endTime, user):

    fixedtask = FixedTask(taskName=taskName, startTime=startTime,
                          endTime=endTime, user=user)
    fixedtask.save(force_insert=True)

    return fixedtask


def generate_unique_user_id():
    length = 6
    while True:
        code = int(uuid4())
        if(not User.objects.filter(userID=code).exists()):
            break
    return code


class Room(models.Model):
    # unique room code
    code = models.CharField(max_length=8, default="", unique=True)
    # unique host of the room
    host = models.CharField(max_length=50, unique=True)
    # can a guest pause the music
    guest_can_pause = models.BooleanField(null=False, default=False)
    # how many votes we need to skip song
    votes_to_skip = models.IntegerField(null=False, default=1)
    # time the room is created, auto_now_add is a DateTimeField specific argument, does what you'd expect
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    # userID = models.IntegerField(null=False, unique=True)
    username = models.CharField(
        max_length=30, default='Default User', unique=True)
    password = models.CharField(max_length=100, null=False, unique=False)
    PreferredMaxConsecutiveTime = models.IntegerField(
        unique=False, validators=[MinValueValidator(0.0)])


class Task(models.Model):
    # taskID = models.IntegerField(null=False, unique=True)
    taskName = models.CharField(max_length=30, default="task")
    dueDate = models.DateTimeField()
    taskLength = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FixedTask(models.Model):
    # fixedtaskID = models.IntegerField(null=False, unique=True)
    taskName = models.CharField(max_length=30, default="fixedtask")
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
