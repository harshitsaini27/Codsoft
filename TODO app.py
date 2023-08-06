import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        task = entry_task.get()
        if task:
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# To-Do list tasks
tasks = []

# Widgets
frame_tasks = tk.Frame(app)
frame_tasks.pack(side=tk.LEFT, padx=10, pady=10)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, selectbackground="black")
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(app, width=50)
entry_task.pack(padx=10, pady=5)

btn_add_task = tk.Button(app, text="Add Task", width=48, command=add_task,bg="lightblue")
btn_add_task.pack(padx=10, pady=5)

btn_remove_task = tk.Button(app, text="Remove Task", width=48, command=remove_task,bg="lightblue")
btn_remove_task.pack(padx=10, pady=5)

btn_update_task = tk.Button(app, text="Update Task", width=48, command=update_task,bg="lightblue")
btn_update_task.pack(padx=10, pady=5)

# Start the application
app.mainloop()

