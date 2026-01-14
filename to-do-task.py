#this is the beginning of the task 
#lets go





import tkinter as tk
from tkinter import messagebox
import sqlite3

# The datatbase info for sqlite3
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL
)
""")
conn.commit()




#Priority Levels: Add a dropdown to mark tasks as Low, Medium, or High priority.

#Due Dates: Use a calendar widget to set deadlines.

#Search Bar: Add a filter to find specific tasks in a long list.