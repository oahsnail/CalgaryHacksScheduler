import datetime
import api
import math

TIME_CHUNK = 15 #the size (in minutes) of the invidually alloted chunks of time

def createSchedule(user):
    myTasks = api.models.Task.objects.filter(user = user).order_by('dueDate') #grabs only the users tasks ans filters them by due date
    lastTaskTime = findLastTask(user)
    arraySize = int(math.ceil((lastTaskTime-datetime.datetime.now())/datetime.timedelta(minutes=TIME_CHUNK)))
    scheduleArray = [None]*arraySize

    #grabs the QuerySet and turns it into a list
    regularTaskList = list()
    for task in myTasks:
        regularTaskList.append(task)

    #subdivides tasks longer than TIME_CHUNK into many TIME_CHUNK sized tasks
    subdividedTaskList = list()
    for task in regularTaskList:
        if task.taskLength < TIME_CHUNK and task.taskLength > 0:
            subdividedTaskList.append(task)
        elif task.taskLength > 0:
            tempTask = api.models.Task(id=api.models.generate_unique_task_id(), taskName = task.taskName, dueDate=(task.dueDate-datetime.timedelta(minutes=TIME_CHUNK)),user = task.user, taskLength = task.taskLength -TIME_CHUNK)
            regularTaskList.append(tempTask)
            tempTask = api.models.Task(id=api.models.generate_unique_task_id(), taskName = task.taskName, dueDate=task.dueDate,user = task.user, taskLength = TIME_CHUNK)
            subdividedTaskList.append(tempTask)

    for task in subdividedTaskList:
        print("Name: "+ str(task.taskName) +"   DueDate: "+ str(task.dueDate) + "   taskLength: " + str(task.taskLength))

    print(arraySize)

def findLastTask(user):
    lastTask = api.models.Task.objects.filter(user = user).latest('dueDate')
    return lastTask.dueDate