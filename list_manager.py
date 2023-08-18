#!/usr/bin/python3
#-*-Coding:utf-8 -*-


# Kreye yon lis vid pou tach yo
todo_list = []

# Fonksyon pou ajoute yon tach nan yon lis
def add_task(description):
    todo_list.append(description)

# Fonksyon pou afiche tach yo
def display_tasks():
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

# Fonksyon pou make tach la fini an
def mark_task_done(index):
    try:
        task = todo_list.pop(index - 1)
        print(f"Tach '{task}' la fini.")
    except IndexError:
        print("Index tach la pa valide.")

# Fonksyon pou anregistre Tache yo
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")
    print("li anrejistre nan 'tasks.txt'.")

# Fonksyon pou chanje Tache yo
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            todo_list.extend([task.strip() for task in tasks])
        print("nou jwenn Tache la depi 'tasks.txt'.")
    except FileNotFoundError:
        print(" Fichye 'tasks.txt' la, pa egziste.")

# Bouk meni an
while True:
    print("\nMeni :")
    print("1. Ajoute tach")
    print("2. Afiche tach yo")
    print("3. Fini yon tach")
    print("4. Anrejistre epi femen ")
    choice = input("Chwazi yon opsyon : ")

    if choice == "1":
        task_description = input("Antre deskripsyonw lan : ")
        add_task(task_description)
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        task_index = int(input("Antre nimewo tach ou vle fini an : "))
        mark_task_done(task_index)
    elif choice == "4":
        save_tasks()
        break

