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

    # check for duplication of the new task based of taskTitle
    if any(task["title"] == taskTitle for task in tasks):
        print(f"{Fore.LIGHTYELLOW_EX}Duplicate task(not added): the task you are trying to add already exists")
        return exit()

    # add ID to each new task being created
    def generateTaskId() -> int:
        newTaskID = tasks[-1]["id"] + 1
        print(f" {Fore.LIGHTMAGENTA_EX}New ID assigned to task: {newTaskID}")
        return newTaskID

    # add the new task to the previous list
    newTask = {"id": generateTaskId(),"title": taskTitle, "completed": isCompleted}
    tasks.append(newTask)

    # write the updated task list to the json file
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print(f"{Fore.LIGHTGREEN_EX}-Task Added-")


def updateTaskCompletion(taskTitle: str, isCompleted: bool):
    # check for existence of tasks.json
    if os.path.isfile("tasks.json") == False:
        print(f"{Fore.LIGHTRED_EX}-No task to mark, you must first add a task-")
        print(f"check the database")
        return exit()
    
    if isCompleted:
        tasks = []

        try: # read/load the tasks from json into a variable
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            print(f"{Fore.LIGHTRED_EX}-No task to mark, you must first add a task-")
            return exit()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

        # mark the task as completed
        for task in tasks:
            if task["title"] == taskTitle and task["completed"] == False:
                task["completed"] = True

                # write the updated task list to the json file
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

                print(f"{Fore.LIGHTGREEN_EX}-Task marked as completed-")
                return
            
            elif task["title"] == taskTitle and task["completed"] == True:
                print(f"{Fore.LIGHTYELLOW_EX}-The task is already marked as completed-")
                break
        else:
            print(f"{Fore.LIGHTRED_EX}-No task exists with the given name-")
    

    elif isCompleted == False:
        try: # read/load the tasks from json into a variable
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            print(f"{Fore.LIGHTRED_EX}-No task to mark, you must first add a task-")
            return exit()
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}An error occurred while loading tasks from JSON:{Fore.RESET}\n{e}")

        # mark the task as uncompleted
        for task in tasks:
            if task["title"] == taskTitle and task["completed"] == True:
                task["completed"] = False

                # write the updated task list to the json file
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file, indent=4)

                print(f"{Fore.LIGHTYELLOW_EX}-Task marked as {Fore.LIGHTRED_EX}un{Fore.RESET}{Fore.LIGHTYELLOW_EX}completed-")
                return
            
            elif task["title"] == taskTitle and task["completed"] == False:
                print(f"{Fore.LIGHTYELLOW_EX}-The task is already marked as uncompleted-")
                break
        else:
            print(f"{Fore.LIGHTRED_EX}-No task exists with the given name-")


#updateTaskCompletion("task4", isCompleted=False)