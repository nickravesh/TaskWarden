import utils
import argparse

parser = argparse.ArgumentParser(description="TaskWarden, A ToDo-List for those who love the command line.")
parser.add_argument("taskTitle", help="the title of task")

args = parser.parse_args()

userTask = args.taskTitle

utils.addTask(userTask)