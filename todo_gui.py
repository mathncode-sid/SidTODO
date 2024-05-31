import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=[todo.strip() for todo in todos])

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit.strip() + "\n")
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=[todo.strip() for todo in todos])
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()
