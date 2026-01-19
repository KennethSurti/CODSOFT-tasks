#need to make a password generator
#user input is lenght of password and complexity 
#result needs to be displayed
#promt the input
#use of combination of random characters


import customtkinter as ctk
import random
import string
from tkinter import messagebox

#checking the libraries compatibility
#Theme

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Password Generator")
app.geometry("500x420")
app.resizable(False, False)

# UI Layout
ctk.CTkLabel(
    app,
    text="🔐 Password Generator",
    font=("Segoe UI", 24, "bold")
).pack(pady=15)

length_entry = ctk.CTkEntry(
    app,
    width=300,
    placeholder_text="Enter password length"
)
length_entry.pack(pady=10)

