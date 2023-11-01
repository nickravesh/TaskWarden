import os
import json
from colorama import init, Fore

init(autoreset=True)

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Define an absolute path to the tasks.json file in the script directory
tasksJson_file = os.path.join(script_dir, "tasks.json")

def addTask(taskTitle: str, isCompleted=False):
    tasks = []

    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        with open(tasksJson_file, "w") as file: file.close()

    try: # read/load the tasks from json into a variable
        with open(tasksJson_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError: pass
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while adding the task:\n{e}")

    # check for duplication of the new task based of taskTitle
    if any(task["title"] == taskTitle for task in tasks):
        print(f"{Fore.LIGHTYELLOW_EX}Duplicate task(not added): the task you are trying to add already exists")
        return exit()

    # add ID to each new task being created
    def generateTaskId() -> int:
        try:
            newTaskID = tasks[-1]["id"] + 1
            print(f" {Fore.LIGHTMAGENTA_EX}New ID assigned to task: {newTaskID}")
            return newTaskID
        except:
            print(f" {Fore.LIGHTMAGENTA_EX}New ID assigned to task: {1}")
            return 1

    # add the new task to the previous list
    newTask = {"id": generateTaskId(),"title": taskTitle, "completed": isCompleted}
    tasks.append(newTask)

    # write the updated task list to the json file
    with open(tasksJson_file, "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"{Fore.LIGHTGREEN_EX}-Task Added-")

# Usage:
#addTask("task2")


def updateTaskCompletion(taskID: int, isCompleted: bool):
    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        print(f"{Fore.LIGHTRED_EX}-No task to mark, you must first add a task-")
        return exit()
    
    if isCompleted:
        tasks = []

        try: # read/load the tasks from json into a variable
            with open(tasksJson_file, "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            print(f"{Fore.LIGHTRED_EX}-No task to mark, you must first add a task-")
            return exit()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

        # mark the task as completed
        for task in tasks:
            if task["id"] == taskID and task["completed"] == False:
                task["completed"] = True

                # write the updated task list to the json file
                with open(tasksJson_file, "w") as file:
                    json.dump(tasks, file, indent=4)

                print(f"{Fore.LIGHTGREEN_EX}-Task marked as completed-")
                return
            
            elif task["id"] == taskID and task["completed"] == True:
                print(f"{Fore.LIGHTYELLOW_EX}-The task is already marked as completed, it will be marked is uncompleted...-")
                # mark the task as uncompleted
                task["completed"] = False

                # write the updated task list to the json file
                with open(tasksJson_file, "w") as file:
                    json.dump(tasks, file, indent=4)

                print(f"{Fore.LIGHTYELLOW_EX}-Task marked as {Fore.LIGHTRED_EX}un{Fore.RESET}{Fore.LIGHTYELLOW_EX}completed-")
                return
        else:
            print(f"{Fore.LIGHTRED_EX}-No task exists with the given ID-")

# Usage:
#updateTaskCompletion(1, isCompleted=True)

def manualSort():
    tasks = []

    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        print(f"{Fore.LIGHTRED_EX}-No task to sort-")
        return exit()
    
    try: # read/load the tasks from json into a variable
        with open(tasksJson_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print(f"{Fore.LIGHTRED_EX}-No task to sort-")
        return exit()
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")


    # sort the tasks: sort the IDs and fill the gap of the deleted task
    for enum, task in enumerate(tasks):
        task["id"] = enum + 1

    # write the updated task list to the json file
    with open(tasksJson_file, "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"{Fore.LIGHTMAGENTA_EX}-Tasks sorted successfully-")
    return


def deleteTask(taskID: int, multiDelete: bool = False):
    tasks = []

    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        print(f"{Fore.LIGHTRED_EX}-No task to delete, you must first add a task-")
        return exit()
    

    try: # read/load the tasks from json into a variable
        with open(tasksJson_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print(f"{Fore.LIGHTRED_EX}-No task to delete, you must first add a task-")
        return exit()
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

    # delete the task based on the given ID
    for task in tasks:
        if task["id"] == taskID:
            tasks.remove(task)
            if multiDelete == False:
                # sort the IDs and fill the gap of the deleted task, because now the IDs sequence is not right
                for enum, task in enumerate(tasks):
                    task["id"] = enum + 1

            # write the updated task list to the json file
            with open(tasksJson_file, "w") as file:
                json.dump(tasks, file, indent=4)

            print(f"{Fore.LIGHTGREEN_EX}-Task deleted successfully-")
            return
    else:
        print(f"{Fore.LIGHTRED_EX}-No task exists with the given ID-")
        return

#deleteTask(3)

def listTask():
    def log(header: str,  rawJson: list, *messages: list):
        strikethrough = "\x1b[9m"
        reset_format = "\x1b[0m"
        
        max_length = max(len(message) for message in messages)
        header_length = len(header)
        box_width = max(max_length + 2, header_length + 2)
        border = '+' + '-' * box_width + '+'

        print(border)
        print(f"| {header:^{box_width-2}} |")
        print(border)
        for message, item in zip(messages, rawJson):
            if item["completed"] == True:
                log_message = f"| {strikethrough}{message:{box_width-2}}{reset_format} |"
                print(log_message)
            else:
                log_message = f"| {message:{box_width-2}} |"
                print(log_message)
        print(border)

    tasks = []

    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        print(f"{Fore.LIGHTRED_EX}-No task to display, you must first add a task-")
        return exit()
    

    try: # read/load the tasks from json into a variable
        with open(tasksJson_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print(f"{Fore.LIGHTRED_EX}-No task to display, you must first add a task-")
        return exit()
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

    try:
        allTasksTitle = []
        for task in tasks:
            allTasksTitle.append(f"{task['id']}  {task['title']}")
        log("TaskWarden", tasks, *allTasksTitle)
    except Exception as e:
        print(e)
        print(f"{Fore.LIGHTRED_EX}-No task to display, you must first add a task-")
# usage:
#listTask()

def sortCompletedTasks():
    tasks = []

    # check for existence of tasks.json
    if os.path.isfile(tasksJson_file) == False:
        print(f"{Fore.LIGHTRED_EX}-No task to sort-")
        return exit()
    
    try: # read/load the tasks from json into a variable
        with open(tasksJson_file, "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print(f"{Fore.LIGHTRED_EX}-No task to sort-")
        return exit()
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

    # sort the completed tasks and move them to the end of the list
    completedTasks = []
    for task in tasks[:]:
        # sort the IDs and fill the gap of the deleted task
        if task["completed"] == True:
            completedTasks.append(task)
            tasks.remove(task)
    tasks.extend(completedTasks)

    # write the updated task list to the json file
    with open(tasksJson_file, "w") as file:
        json.dump(tasks, file, indent=4)

    # sort the tasks IDs
    manualSort()
    return
# Usage:
#sortCompletedTasks()