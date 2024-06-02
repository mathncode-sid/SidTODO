import streamlit as st

import functions

todos = functions.get_todos()

st.title("TODO APP")
st.subheader("This is my TODO App")
st.write("This is a simple app to enhance your productivity")


st.checkbox("Buy Grocery")
st.checkbox("Throw the trash")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo")