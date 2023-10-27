# TaskWarden

**Your To-Do list, the command-line way.**

![TaskWardenGif](https://github.com/nickravesh/TaskWarden/blob/master/assets/demo.gif)

### The motivation behind it

> The need for a straightforward command-line based To-Do list with focus on simplicity and ease of use, yet appealing to the eye.

## Features

- **Command-Line Simplicity:** Manage your tasks effortlessly via the command line.

- **Add & Organize Tasks:** Easily add single or multiple tasks and maintain a sorted list.

- **Mark & Unmark Tasks:** Keep track of task completion status, mark or unmark single or multiple tasks with only one command.

- **Efficient Deletion:** Remove tasks individually or in bulk without hassle.

- **Visual Task List:** View and differentiate tasks with a visually pleasing list.

- **Prevent Duplication:** TaskWarden guards against adding duplicate tasks.

For detailed usage instructions, see the [Usage](#usage) section below.


## Requirements

Not much, just the `coloroma` to print colored logs for you:
```bash
pip3 install colorama
```
**Note:** If you want to use the installer, it will take care of the requirements itself, so you can forget about this step...

## One-Liner install for Debian-based distros

```bash
  curl -Ls https://github.com/nickravesh/TaskWarden/archive/master.tar.gz | tar -xz && cd TaskWarden-master && bash install.sh
```

## Usage
| **Subcommand** | **Description** | **Example** | **MultipleTasks** |
|----------------|-----------------|-------------|-------------------|
| add [taskTitle]| add new task(s) | tw add "review the code"| tw add "debug foo" "commit the changes" |
| done [taskID)]| mark task(s) as done/undone | tw done 1 | tw done 3 5 9 |
| rm [taskID] | remove task(s) | tw rm 1 | tw rm 2 4 8 |
| ls | list the tasks | tw ls | -

**Note:** You can also use `TaskWarden`, `taskwarden` or even `todo` instead of `tw` if you like.

## Contributing	

Contributions are always welcome!  
Let me know if you have any suggestions, or open an issue if you have faced any problems.

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://opensource.org/licenses/)

[![](https://visitcount.itsvg.in/api?id=taskwarden&label=Repository%20Views&icon=0&pretty=true)](https://visitcount.itsvg.in)