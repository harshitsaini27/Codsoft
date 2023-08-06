import tkinter as tk
from tkinter import ttk
import random
import string
# import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("400x200")

        self.length_label = ttk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_var = tk.IntVar(value=12)
        self.length_entry = ttk.Entry(root, textvariable=self.length_var, width=5)
        self.length_entry.pack(pady=5)

        self.complexity_label = ttk.Label(root, text="Password Complexity:")
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar(value="Medium")
        self.complexity_combobox = ttk.Combobox(root, textvariable=self.complexity_var, values=["Low", "Medium", "High"])
        self.complexity_combobox.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="Generated Password:")
        self.result_label.pack(pady=5)

        self.result_var = tk.StringVar(value="")
        self.result_entry = ttk.Entry(root, textvariable=self.result_var, state="readonly", width=30)
        self.result_entry.pack(pady=5)

    def generate_password(self):
        password_length = self.length_var.get()
        complexity = self.complexity_var.get()
        password_characters = ""

        if complexity == "Low":
            password_characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            password_characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            password_characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

        password = "".join(random.choice(password_characters) for _ in range(password_length))
        self.result_var.set(password)
        pyperclip.copy(password)  # Copy the password to the clipboard

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
