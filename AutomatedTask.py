#I am going to create a schedule tracker that keeps track of daily task

tasks = []
print("Welcome to Schedule Tracker")
numOfTasks = input("How many tasks do you have for today?")
print("You will now be asked for " + numOfTasks + " tasks that you want to accomplish today")
for i in range(int(numOfTasks)) :
    t = input("What is a task that you want to accomplish today? >> ")
    time = input("When do you want to accomplish this task by? >> ")
    fullTask = str(t + " -> @" + time)
    tasks.append(fullTask)

print("\nHere is your schedule for today: ")
for x in range(len(tasks)) :
    print(tasks[x])