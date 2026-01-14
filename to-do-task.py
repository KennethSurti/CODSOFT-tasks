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
#keep track of tasks

def load_tasks():
    task_list.delete("1.0", "end")
    cursor.execute("SELECT * FROM tasks")
    for task in cursor.fetchall():
        task_list.insert(
            "end",
            f"{task[0]}. {task[1]}  [{task[2]}]\n"
        )

#add task

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

# tracking tasks
def get_selected_task_id():
    try:
        selected_line = task_list.get("insert linestart", "insert lineend")
        return selected_line.split(".")[0]
    except:
        return None

def mark_completed():
    task_id = get_selected_task_id()
    if not task_id:
        messagebox.showwarning("Selection Error", "Select a task line")
        return

    cursor.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        ("Completed", task_id)
    )
    conn.commit()
    load_tasks()

#deletion of tasks

def delete_task():
    task_id = get_selected_task_id()
    if not task_id:
        messagebox.showwarning("Selection Error", "Select a task line")
        return

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    load_tasks()    

# UI LAYOUT

#HEADER
title_label = ctk.CTkLabel(
    app,
    text="📝 To-Do List",
    font=("Segoe UI", 26, "bold")
)
title_label.pack(pady=15)

task_entry = ctk.CTkEntry(
    app,
    width=400,
    height=40,
    placeholder_text="Enter a new task..."
)
task_entry.pack(pady=10)


# Button control
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=10)

ctk.CTkButton(
    button_frame,
    text="Add Task",
    width=120,
    command=add_task
).grid(row=0, column=0, padx=10)

ctk.CTkButton(
    button_frame,
    text="Mark Completed",
    width=120,
    fg_color="#008000",
    hover_color="#008000",
    command=mark_completed
).grid(row=0, column=1, padx=10)

ctk.CTkButton(
    button_frame,
    text="Delete Task",
    width=120,
    fg_color="#b52b2b",
    hover_color="#8f1f1f",
    command=delete_task
).grid(row=0, column=2, padx=10)


#Input Box


task_list = ctk.CTkTextbox(
    app,
    width=460,
    height=260,
    corner_radius=10
)
task_list.pack(pady=15)

load_tasks()

# Application Loop 

app.mainloop()
conn.close()



#Priority Levels: Add a dropdown to mark tasks as Low, Medium, or High priority.

#Due Dates: Use a calendar widget to set deadlines.

#Search Bar: Add a filter to find specific tasks in a long list.