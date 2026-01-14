#this is the beginning of the task 
#lets go


import customtkinter as ctk
import sqlite3
import os
from tkinter import messagebox

# Database info 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "todo.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
conn.commit()

#Theme of window
 
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#window settings
app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("520x500")
app.resizable(False, False)


#CRUD operations

def load_tasks():
    task_list.delete("1.0", "end")
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        task_list.insert(
            "end",
            f"{task[0]}. {task[1]}  [{task[2]}]\n"
        )


def add_task():
    title = task_entry.get().strip()
    if not title:
        messagebox.showwarning("Input Error", "Task cannot be empty")
        return

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, "Pending")
    )
    conn.commit()
    task_entry.delete(0, "end")
    load_tasks()


#Priority Levels: Add a dropdown to mark tasks as Low, Medium, or High priority.

#Due Dates: Use a calendar widget to set deadlines.

#Search Bar: Add a filter to find specific tasks in a long list.