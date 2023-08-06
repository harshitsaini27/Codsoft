import tkinter as tk

def evaluate_expression():
    try:
        result = eval(expression.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error: " + str(e))

def on_button_click(event):
    current_char = event.widget.cget("text")
    current_expression = expression.get()

    if current_char == "=":
        evaluate_expression()
    elif current_char == "C":
        expression.set("")
        result_label.config(text="Result: ")
    else:
        expression.set(current_expression + current_char)

# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.config(bg="#EDEDED")

# Create a variable to store the expression
expression = tk.StringVar()

# Entry widget to display the expression
expression_entry = tk.Entry(root, textvar=expression, font=("Arial", 20), justify="right")
expression_entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Frame to hold the calculator buttons
button_frame = tk.Frame(root, bg="#EDEDED")
button_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Buttons for digits and operators
buttons = [
    ("7", "8", "9", "+"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "*"),
    ("C", "0", "=", "/")
]

for row_idx, row in enumerate(buttons):
    for col_idx, char in enumerate(row):
        btn = tk.Button(button_frame, text=char, font=("Arial", 18), bg="#A8DADC", fg="#333333", relief=tk.GROOVE)
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", on_button_click)

# Make the buttons expand and fill the grid cells
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Result label to display the calculated result
result_label = tk.Label(root, text="Result: ", font=("Arial", 16), bg="#EDEDED")
result_label.pack(pady=5)

root.mainloop()
