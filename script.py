tasks = []

def addtask():
    task = input("Please enter a task")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listtask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks")
        for x, task in enumerate (tasks):
            print (f"Task #{x}. {task}")

def deletetask():
    listtask()
    try:
        tasktoDelete = int(input("enter the # to delete: "))
        if tasktoDelete < len(tasks) and tasktoDelete>=0 :
            tasks.pop(tasktoDelete)
            print(f"Task #{tasktoDelete}has been removed")
        else:
            print(f"Task #{tasktoDelete} was not found")
    except:
        print("Invalid input")

if __name__ == "__main__":
    print ("wELCOME! TO THE TO DO LIST APP")
    while True:
        print("/n")
        print("Please select one of the following option ?")
        print("-------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            addtask()
        elif (choice == "2"):
            deletetask()
        elif (choice == "3"):
            listtask()
        elif (choice == "4"):
            break
        else :
            print("Invalid Input. Please Try again")
    print (" GOODBYE :)")