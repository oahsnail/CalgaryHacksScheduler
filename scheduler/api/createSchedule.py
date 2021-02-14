from .models import Room, User
import datetime

def createSchedule(self):
    myTasks = Task.objects.filter(userID = self.userID).order_by('dueDate')
    lastTaskTime = findLastTask(self)
    arraySize = int(((datetime.datetime.now()-lastTaskTime)/timedelta(minutes=15)))
    scheduleArray = [None]*arraySize
    for task in myTasks:
        

def findLastTask(self):
    lastTask = Task.objects.filter(userID = self.userID).latest('dueDate')
    return lastTask.dueDate