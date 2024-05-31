import functions
import PySimpleGUI as sg
import time

sg.theme("DarkGrey10")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
complete_button = sg.Button(size=12, image_source="complete.png", mouseover_colors="LightBlue2",
                            tooltip="Complete Todo Item", key="Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
window_open = True
while window_open:
    event, values = window.read(timeout=250)
    if event == sg.WINDOW_CLOSED:
        window_open = False
    else:
        window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
        match event:
            case "Add":
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=[todo.strip() for todo in todos])

            case "Edit":
                try:
                    todo_to_edit = values['todos'][0]
                    new_todo = values['todo']

                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit.strip() + "\n")
                    todos[index] = new_todo + "\n"
                    functions.write_todos(todos)
                    window['todos'].update(values=[todo.strip() for todo in todos])
                except IndexError:
                    sg.popup("Please select an item first", font=('Helvetica', 20))
            case "Complete":
                try:
                    todo_to_complete = values['todos'][0]
                    todos = functions.get_todos()
                    todos.remove(todo_to_complete)
                    functions.write_todos(todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')
                except IndexError:
                    sg.popup("Please select an item first", font=('Helvetica', 20))
            case "Exit":
                break
            case 'todos':
                window['todo'].update(value=values['todos'][0])

window.close()
