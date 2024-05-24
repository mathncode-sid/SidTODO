def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            print("Got it!")
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos_arg=todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            if len(user_action) > 9:
                number = int(user_action[9:])
            else:
                print("Please specify a number to complete.")
                continue

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos_arg=todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("The item is not in the todo")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Adios")
