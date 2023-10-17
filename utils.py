import os
import json
from colorama import init, Fore

init(autoreset=True)

def addTask(taskTitle: str, isCompleted=False):
    tasks = []

    # check for existence of tasks.json
    if os.path.isfile("tasks.json") == False:
        with open("tasks.json", "w") as file: file.close()

    try: # read/load the tasks from json into a variable
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError: pass
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while adding the task:\n{e}")

    # add the new task to the previous list
    newTask = {"title": taskTitle, "completed": isCompleted}
    tasks.append(newTask)

    # write the updated task list to the json file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"{Fore.LIGHTGREEN_EX}-Task Added-")
