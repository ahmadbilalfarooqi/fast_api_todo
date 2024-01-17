# streamlit_client.py

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App by Ahmad Bilal")

def create_todo():
    name = st.text_input("Enter Todo")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"name": name, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")
            
            
def update_todo():
    todo_id = st.number_input("Update Todo")
    name = st.text_input(f"Enter Todo Name ({todo_id})", key=f"name_{todo_id}")
    description = st.text_area(f"Enter Todo Description ({todo_id})", key=f"description_{todo_id}")
    if st.button("Update Todo"):
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"name": name, "description": description})
        if response.status_code == 200:
            st.success("Todo updated successfully")

def delete_todo():
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")

if __name__ == "__main__":
    create_todo()
    update_todo()
    delete_todo()