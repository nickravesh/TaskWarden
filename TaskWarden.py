import utils
import argparse

parser = argparse.ArgumentParser(description="TaskWarden, A ToDo-List for those who love the command line.")
subParsers = parser.add_subparsers(title="Subcommands", help="Standard operations")
# define sub-parser for adding task
addTask_Subparser = subParsers.add_parser("add", help="add new tasks to TaskWarden")
addTask_Subparser.add_argument("add", type=str, nargs="*", help="add new tasks to TaskWarden")
# define sub-parser for marking task as completed/uncompleted
doneTask_Subparser = subParsers.add_parser("done", help="mark tasks as completed/uncompleted")
doneTask_Subparser.add_argument("done", type=int, nargs="*", help="mark tasks as completed/uncompleted")
# define sub-parser for removing task
removeTask_Subparser = subParsers.add_parser("rm", help="remove tasks from TaskWarden")
removeTask_Subparser.add_argument("rm", type=int, nargs="*", help="remove tasks from TaskWarden")
# define sub-parser for listing tasks
listTask_Subparser = subParsers.add_parser("ls", help="display the list of existing tasks")
listTask_Subparser.add_argument("ls", action="store_true", help="display the list of existing tasks")
# define sub-parser for sorting completed tasks
sortTask_Subparser = subParsers.add_parser("sort", help="sort the completed tasks to the end of the list")
sortTask_Subparser.add_argument("sort", action="store_true", help="sort the completed tasks to the end of the list")
# define sub-parser for deleting completed tasks
sortTask_Subparser = subParsers.add_parser("refresh", help="delete the completed tasks")
sortTask_Subparser.add_argument("refresh", action="store_true", help="delete the completed tasks")

args = parser.parse_args()

if hasattr(args, "add"):
    if args.add != None:
        for taskName in args.add:
            utils.addTask(taskName)
elif hasattr(args, "done"):
    if args.done != None:
        for taskID in args.done:
            utils.updateTaskCompletion(taskID, True)
    else:
        # TODO: open questionary and ask the user which task they completed
        pass
elif hasattr(args, "rm"):
    if args.rm != None and len(args.rm) > 1:
        for taskID in args.rm:
            utils.deleteTask(taskID, True)
        utils.manualSort()
    elif args.rm != None and len(args.rm) == 1:
        for taskID in args.rm:
            utils.deleteTask(taskID, False)
elif hasattr(args, "ls"):
    if args.ls:
        utils.listTask()
elif hasattr(args, "sort"):
    if args.sort:
        utils.sortCompletedTasks()
elif hasattr(args, "refresh"):
    if args.refresh:
        utils.deleteCompletedTasks()

else:
    parser.print_help()
