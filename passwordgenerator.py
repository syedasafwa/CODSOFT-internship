# Task 3: Password Generator with Tkinter GUI
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        strength = strength_var.get()

        if strength == "Simple":
            chars = string.ascii_lowercase
        elif strength == "Medium":
            chars = string.ascii_letters + string.digits
        else:  # Strong
            chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)

# Password Length
tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Strength Option
tk.Label(root, text="Select Strength:").pack(pady=5)
strength_var = tk.StringVar(value="Strong")
strength_menu = tk.OptionMenu(root, strength_var, "Simple", "Medium", "Strong")
strength_menu.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Result Display
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=40, state="readonly").pack(pady=5)

# Run App
root.mainloop()
