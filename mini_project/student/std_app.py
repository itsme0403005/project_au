
import tkinter as tk
from tkinter import messagebox
from storage import std_data, load_data
from student import students

def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    marks = entry_marks.get()
    if not name or not roll or not marks:
        messagebox.showerror("Error", "All fields are required")
        return
    try:
        roll = int(roll)
        marks = int(marks)
    except ValueError:
        messagebox.showerror("Error", "Roll and Marks must be numbers")
        return
    
    student = students(name, roll, marks)
    std_data(student)
    messagebox.showinfo("Success", f"Student {name} added!")
    entry_name.delete(0, tk.END)
    entry_roll.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

def view_students():
    top = tk.Toplevel(root)
    top.title("Student List")

    data = load_data(return_data=True)

    if not data:
        tk.Label(top, text="No students found.").pack()
        return

    for idx, student in enumerate(data, start=1):
        tk.Label(top, text=f"{idx}. {student.display()}").pack()


root = tk.Tk()
root.title("Student Management System")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Roll Number:").grid(row=1, column=0)
entry_roll = tk.Entry(root)
entry_roll.grid(row=1, column=1)

tk.Label(root, text="Marks:").grid(row=2, column=0)
entry_marks = tk.Entry(root)
entry_marks.grid(row=2, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=3, column=0, pady=10)
tk.Button(root, text="View Students", command=view_students).grid(row=3, column=1, pady=10)

root.mainloop()
