import requests

SERVER_URL = 'http://127.0.0.1:5000'

def addtask(task):
    try:
        response = requests.post(f"{SERVER_URL}/tasks", json={'task': task})
        response.raise_for_status()
        print("Task added.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def removetask(task):
    try:
        response = requests.delete(f"{SERVER_URL}/tasks", json={'task': task})
        response.raise_for_status()
        print("Task removed.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def displaytasks():
    try:
        response = requests.get(f"{SERVER_URL}/tasks")
        response.raise_for_status()
        tasks = response.json()
        print("To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def savetasks():
    try:
        response = requests.post(f"{SERVER_URL}/tasks/save")
        response.raise_for_status()
        print("Tasks saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def loadtasks():
    try:
        response = requests.get(f"{SERVER_URL}/tasks/load")
        response.raise_for_status()
        print("Tasks loaded successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

loadtasks()
while True:
    print("\nOptions: add, remove, display, save, exit")
    choice = input("Choose an option: ").strip().lower()
    
    if choice == "add":
        task = input("Enter a task: ").strip()
        addtask(task)
    elif choice == "remove":
        task = input("Enter a task to remove: ").strip()
        removetask(task)
    elif choice == "display":
        displaytasks()
    elif choice == "save":
        savetasks()
    elif choice == "exit":
        savetasks()
        break
    else:
        print("Invalid option.")
