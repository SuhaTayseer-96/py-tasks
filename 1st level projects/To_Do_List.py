tasks = []
def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("\n task: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully.")

def delete_task():
    show_tasks()
try:
    task_num = int(input("Number of tasks to delete: "))
    if 1 <= task_num <= len(tasks):
        remove_task = tasks.pop(task_num - 1)
        print(f"Task '{remove_task}' deleted successfully.")
    else:
        print("Invalid task number.")
except ValueError:
    print("Invalid task number")

while True:
     print("\n order list: ")
     print("1. show tasks")
     print("2. add task")
     print("3. delete task")
     print("4. exit")
     choice = input("Enter your choice (1-4): ")
     if choice == "1":
          show_tasks()
     elif choice == "2":
          add_task()
     elif choice == "3":
           delete_task()
     elif choice == "4":
            print("Goodbye")
            break
     else:
        print("Invalid choice")
 
