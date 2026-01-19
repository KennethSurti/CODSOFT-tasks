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

# Complexity Options

lowercase_var = ctk.BooleanVar(value=True)
uppercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=False)

options_frame = ctk.CTkFrame(app)
options_frame.pack(pady=10)

ctk.CTkCheckBox(options_frame, text="Lowercase (a-z)", variable=lowercase_var).grid(row=0, column=0, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Uppercase (A-Z)", variable=uppercase_var).grid(row=0, column=1, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Digits (0-9)", variable=digits_var).grid(row=1, column=0, padx=10, pady=5)
ctk.CTkCheckBox(options_frame, text="Symbols (!@#$)", variable=symbols_var).grid(row=1, column=1, padx=10, pady=5)

# Fuctions for generation

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid password length")
        return
    
    characters = ""

    if lowercase_var.get():
        characters += string.ascii_lowercase
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if digits_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

#Exceptions and result review 
    if characters == "":
        messagebox.showwarning("Selection Error", "Select at least one complexity option")
        return

    password = ''.join(random.choice(characters) for _ in range(length))

    result_entry.configure(state="normal")
    result_entry.delete(0, "end")
    result_entry.insert(0, password)
    result_entry.configure(state="readonly")


#result declaration and buttons

ctk.CTkButton(
    app,
    text="Generate Password",
    command=generate_password
).pack(pady=15)

result_entry = ctk.CTkEntry(
    app,
    width=380,
    state="readonly"
)
result_entry.pack(pady=10)

app.mainloop()