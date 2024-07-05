import requests

SERVER_URL = 'http://127.0.0.1:5000'

def add_task(task):
    try:
        response = requests.post(f"{SERVER_URL}/tasks", json={'task': task})
        response.raise_for_status()
        print("Task added successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error adding task: {e}")

def remove_task(task):
    try:
        response = requests.delete(f"{SERVER_URL}/tasks", json={'task': task})
        response.raise_for_status()
        print("Task removed successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error removing task: {e}")

def display_tasks():
    try:
        response = requests.get(f"{SERVER_URL}/tasks")
        response.raise_for_status()
        tasks = response.json()
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving tasks: {e}")

def save_tasks():
    try:
        response = requests.post(f"{SERVER_URL}/tasks/save")
        response.raise_for_status()
        print("Tasks saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error saving tasks: {e}")

def load_tasks():
    try:
        response = requests.get(f"{SERVER_URL}/tasks/load")
        response.raise_for_status()
        print("Tasks loaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error loading tasks: {e}")

load_tasks()
while True:
    print("\nOptions: add, remove, display, save, exit")
    choice = input("Choose an option: ").strip().lower()
    
    if choice == "add":
        task = input("Enter a task: ").strip()
        add_task(task)
    elif choice == "remove":
        task = input("Enter a task to remove: ").strip()
        remove_task(task)
    elif choice == "display":
        display_tasks()
    elif choice == "save":
        save_tasks()
    elif choice == "exit":
        save_tasks()
        break
    else:
        print("Invalid option.")

