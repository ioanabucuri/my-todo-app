import streamlit as st
import functions

def add_todo():
    # we take the value from the widget having key=new_todo
    # session_state is an object which looks like a dictionary
    #and contains pairs of data that the user enters using the keys
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo..", on_change=add_todo, key="new_todo")
