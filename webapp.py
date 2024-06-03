import streamlit as st
import os

import functions

os.chdir(os.path.dirname(os.path.realpath(__file__)))
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def mark_complete(event, todo):
    completed_todos.append(todo)
    todos.remove(todo)
    functions.write_todos(todos)
    del st.session_state[todo]


todos = functions.get_todos()
completed_todos = functions.get_completed_todos()

st.title("TODO APP")
st.subheader("This is my TODO App")
st.write("This is a simple app to enhance your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        st.session_state["todo_to_complete"] = todo
        if st.button("Complete", on_click=mark_complete, args=(todo, todo)):
            st.session_state["todo_to_complete"] = todo

for completed_todo in completed_todos:
    st.write(completed_todo)
st.text_input(label="TODO", placeholder="Add new todo",
              on_change=add_todo, key='new_todo', label_visibility="hidden")
st.button("Add", on_click=add_todo)
