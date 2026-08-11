tasks=[]
#Add Tasks
def add_task():
    user_enter=input("Enter Todays Task : ")
    tasks.append(user_enter)
    print("Tasks added successfully")
    

#View Tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        index = 0
        while index < len(tasks):
            print(index + 1, ".", tasks[index])
            index = index + 1
#delete task 
def delete_tasks():
    if len(tasks) == 0:
        print("No tasks available to delete.")
    else:
        print("\nYour Tasks:")
        index = 0
        while index < len(tasks):
            print(index + 1, ".", tasks[index])
            index = index + 1
        try:
            task_number = int(input("Enter task number to delete: "))
            index = task_number - 1
            tasks.pop(index)
            print("Task deleted successfully!")
        except ValueError:
            print("Value Error")
        except IndexError:
            print("Index Error .. Select Again")
       

#pop() → removes an item using its index
#remove() → removes an item by its value
