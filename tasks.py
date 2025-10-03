from storage import load_task, save_tasks

def add_task(tasks):
    user_task = input("Enter task: ").strip()
    if user_task:
        tasks.append({"Task": user_task, "Done": False})
        save_tasks(tasks)
        print("Task added successfully") 
