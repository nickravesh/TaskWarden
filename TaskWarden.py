import utils
import argparse

parser = argparse.ArgumentParser(description="TaskWarden, A ToDo-List for those who love the command line.")
subParsers = parser.add_subparsers(title="Subcommands", help="Standard operations")
# define sub-parser for adding task
addTask_Subparser = subParsers.add_parser("add", help="add a new task to TaskWarden")
addTask_Subparser.add_argument("add", type=str, nargs="?", help="add a new task to TaskWarden")
# define sub-parser for marking task as completed/uncompleted
doneTask_Subparser = subParsers.add_parser("done", help="mark task as completed/uncompleted")
doneTask_Subparser.add_argument("done", type=int, nargs="?", help="mark task as completed/uncompleted")
# define sub-parser for removing task
removeTask_Subparser = subParsers.add_parser("rm", help="remove a task from TaskWarden")
removeTask_Subparser.add_argument("rm", type=int, nargs="?", help="remove a task from TaskWarden")
# define sub-parser for listing tasks
listTask_Subparser = subParsers.add_parser("ls", help="display the list of existing tasks")
listTask_Subparser.add_argument("ls", action="store_true", help="display the list of existing tasks")

args = parser.parse_args()

if hasattr(args, "add"):
    if args.add != None:
        utils.addTask(args.add)
elif hasattr(args, "done"):
    if args.done != None:
        utils.updateTaskCompletion(args.done, True)
    else:
        # TODO: open questionary and ask the user which task they completed
        pass
elif hasattr(args, "rm"):
    if args.rm != None:
        utils.deleteTask(args.rm)
elif hasattr(args, "ls"):
    if args.ls:
        utils.listTask()

else:
    parser.print_help()
