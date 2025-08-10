import tkinter as tk
import math

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def backspace():
    current = entry.get()
    entry.delete(len(current) - 1)

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def add_pi():
    entry.insert(tk.END, math.pi)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg='lightgrey')  # Set background color

# Create entry widget
entry = tk.Entry(root, width=20, font=('Arial', 16), bg='lavender', fg='black')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('AC', 5, 0), ('<-', 5, 1), ('√', 5, 2), ('π', 5, 3)  # All Clear, Backspace, Square Root, Pi buttons
]

# Add buttons to the window
for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), bg='lightyellow' if text in ['=', '.','<-','√','π','AC'] else 'gray' if text.isdigit() else 'black', fg='black' if text in ['=', '.','<-','√','π','AC'] else 'white')
    if text == 'AC':
        btn.config(command=clear)
    elif text == '=':
        btn.config(command=calculate)
    elif text == '<-':
        btn.config(command=backspace)
    elif text == '√':
        btn.config(command=square_root)
    elif text == 'π':
        btn.config(command=add_pi)
    else:
        btn.config(command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
