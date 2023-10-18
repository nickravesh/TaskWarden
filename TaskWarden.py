import utils
import argparse

parser = argparse.ArgumentParser(description="TaskWarden, A ToDo-List for those who love the command line.")
parser.add_argument("taskTitle", type=str, nargs="?", help="the title of task")
parser.add_argument("-d", "--done", action="store_true", help="mark task as completed/uncompleted")
args = parser.parse_args()

if args.done and args.done:
    # If -d is provided along with a taskTitle, mark the task as completed
    utils.updateTaskCompletion(args.taskTitle, True)
elif args.taskTitle:
    # If only a taskTitle is provided, add the task
    utils.addTask(args.taskTitle)
else:
    # Handle the case where no arguments are provided
    parser.print_help()