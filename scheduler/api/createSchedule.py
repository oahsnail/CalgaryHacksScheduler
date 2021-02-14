from .models import *
import datetime

TIME_CHUNK = 15


def createSchedule(user):
    myTasks = models.Task.objects.filter(user=user).order_by('dueDate')
    lastTaskTime = findLastTask(user)
    arraySize = int(((lastTaskTime-datetime.datetime.now()) /
                     datetime.timedelta(minutes=TIME_CHUNK)))
    scheduleArray = [None]*arraySize
    regularTaskList = list()
    for task in myTasks:
        regularTaskList.append(task)

    subdividedTaskList = list()
    for task in regularTaskList:
        if task.taskLength < TIME_CHUNK:
            subdividedTaskList.append(task)
        elif task.taskLength > 0:
            tempTask = models.Task(id=models.generate_unique_task_id(), taskName=task.taskName, dueDate=(
                task.dueDate-datetime.timedelta(minutes=TIME_CHUNK)), user=task.user, taskLength=task.taskLength - TIME_CHUNK)
            regularTaskList.append(tempTask)
            tempTask = models.Task(id=models.generate_unique_task_id(
            ), taskName=task.taskName, dueDate=task.dueDate, user=task.user, taskLength=TIME_CHUNK)
            subdividedTaskList.append(tempTask)


def findLastTask(user):
    lastTask = Task.objects.filter(user=user).latest('dueDate')
    return lastTask.dueDate
