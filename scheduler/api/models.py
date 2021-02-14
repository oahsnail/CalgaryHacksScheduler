from django.db import models
import string
import random
from django.core.validators import MinValueValidator

# Create your models here.
# a model is basicaly a sql table, but django specific abstraction
# see this page for some sql/models side by sides: https://docs.djangoproject.com/en/3.1/topics/db/models/
# Also, here are all the info about fields and field types in django: https://docs.djangoproject.com/en/3.1/ref/models/fields/

# here we're basically specifying a Room model/db table that contains the info and some rules about that room.

# basic rule: fat models, and thin views.


# test model, not a actual one we use
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

    def generate_unique_code(self):
        length = 6
        while True:
            code = ''.join(random.choices(string.ascii_uppercase, k=length))
            # this is actually kind of a query, learn more and compare to SQL here:
            # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.count
            if Room.objects.filter(code=code).count() == 0:
                # or alternatively: if(not Room.objects.filter(code=code).exists():)
                break
        return code


class User(models.Model):
    userID = models.IntegerField(null=False, unique=True)
    name = models.CharField(
        max_length=30, default='Default User', unique=False)
    prefPreferedMaxConsecutiveTime = models.IntegerField(
        unique=False, validators=[MinValueValidator(0.0)])


class Task(models.Model):
    taskID = models.IntegerField(null=False, unique=True)
    taskName = models.CharField(max_length=30, default="task")
    dueDate = models.DateTimeField()
    userID = models.ForeignKey("task", on_delete=models.CASCADE)


class FixedTask(models.Model):
    fixedtaskID = models.IntegerField(null=False, unique=True)
    taskName = models.CharField(max_length=30, default="task")
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    userID = models.ForeignKey("task", on_delete=models.CASCADE)
