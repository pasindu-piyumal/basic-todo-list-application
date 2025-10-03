import json
import os

taskFile = "Task.json"

def load_task():
    if os.path.exists(taskFile):
        with open(taskFile, "r") as file:
            return json.load(taskFile)
    return []

def save_tasks(tasks):
    with open(taskFile, "w") as file:
        json.dump(tasks, file, indent=4)