import tkinter as tk
from tkinter import ttk

# Define the operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

# Function to perform the selected operation
def perform_operation():
    num1 = float(number1_entry.get())
    num2 = float(number2_entry.get())
    choice = operation_var.get()
    if choice == '+':
        result = add(num1, num2)
    elif choice == '-':
        result = subtract(num1, num2)
    elif choice == '*':
        result = multiply(num1, num2)
    elif choice == '/':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"
    result_label.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and pack the widgets
number1_label = ttk.Label(root, text="Enter first number:")
number1_label.pack()

number1_entry = ttk.Entry(root)
number1_entry.pack()

number2_label = ttk.Label(root, text="Enter second number:")
number2_label.pack()

number2_entry = ttk.Entry(root)
number2_entry.pack()

operation_var = tk.StringVar()
operation_combo = ttk.Combobox(root, textvariable=operation_var)
operation_combo['values'] = ('+', '-', '*', '/')
operation_combo['state'] = 'readonly'  # Prevents user typing a value
operation_combo.pack()

calculate_button = ttk.Button(root, text="Calculate", command=perform_operation)
calculate_button.pack()

result_label = ttk.Label(root, text="Result: ")
result_label.pack()

# Start the GUI event loop
root.mainloop()
