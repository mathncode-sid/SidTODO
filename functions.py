def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def get_completed_todos(filepath="completed_todos.txt"):
    """ Read a text file and return the list of
    completed to-do items.
    """
    with open(filepath, 'r') as file_local:
        completed_todos_local = file_local.readlines()
    return completed_todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write a to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def write_completed_todos(completed_todos_arg, filepath="completed_todos.txt"):
    """ Write a completed to-do items list in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(completed_todos_arg)

