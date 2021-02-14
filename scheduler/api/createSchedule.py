from .models import Room, User
import datetime

def createSchedule(self):
    myTasks = Task.objects.filter(user_id = self.user_id).order_by('dueDate')
    lastTaskTime = findLastTask(self)
    arraySize = int(((lastTaskTime-datetime.datetime.now())/datetime.timedelta(minutes=15)))
    scheduleArray = [None]*arraySize
    regularTaskList = list()
    for task in myTasks:
        regularTaskList.append(task)
    subdividedTaskList = list()
    for task in myTasks:
        if task.taskLength < 15:
            myTaskList.append(task)
        else:
            tempTask = 

        
        

def findLastTask(self):
    lastTask = Task.objects.filter(userID = self.userID).latest('dueDate')
    return lastTask.dueDate