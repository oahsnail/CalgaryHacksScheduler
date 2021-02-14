import api
import datetime

# Deletes old models
api.models.User.objects.all().delete()
api.models.Task.objects.all().delete()

tomorrow = datetime.datetime.now()+datetime.timedelta(days=1, minutes=10)

#creates test users and assignments
u1 = api.models.User(id=1,username="pami", password="aidkhfgSKHVsjk", PreferredMaxConsecutiveTime=3)
u1.save()
u2 = api.models.User(id=2,username="lian", password="rhgilwerghdsfg", PreferredMaxConsecutiveTime=5)
u2.save()

t1 = api.models.Task(id=1,taskName="science project",dueDate=tomorrow, user = u1,taskLength=60)
t1.save()
t2 = api.models.Task(id=2,taskName="math project",dueDate=tomorrow, user = u1,taskLength=45)
t2.save()
t3 = api.models.Task(id=3,taskName="l.a. project",dueDate=tomorrow, user = u2,taskLength=50)
t3.save()
t4 = api.models.Task(id=4,taskName="lick obamas toes",dueDate=tomorrow, user = u1,taskLength=12)
t4.save()
t5 = api.models.Task(id=5,taskName="eat obamas toe gunk",dueDate=tomorrow, user = u1,taskLength=150)
t5.save()
t6 = api.models.Task(id=6,taskName="ask lians mom on a date",dueDate=tomorrow, user = u1,taskLength=69)
t6.save()

for task in myTasks:
    regularTaskList.append(task)

for task in subdividedTaskList:
    print("Name: "+ str(task.taskName) +"   DueDate: "+ str(task.dueDate) + "   taskLength: " + str(task.taskLength))