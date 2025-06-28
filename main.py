import tkinter as tk
from tkinter import messagebox
from college.cutoff_calculator import CutoffCalculator
from college.admission import CourseSelection
from college.application_form import display_form
import random
from database import create_database, insert_application
def submit_form():
    try:
        name = name_entry.get()
        fname = fname_entry.get()
        age = int(age_entry.get())
        caste = caste_entry.get().upper()
        math = int(math_entry.get())
        phy = int(phy_entry.get())
        chem = int(chem_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for Age, Maths, Physics, and Chemistry marks.")
        return

    calculator = CutoffCalculator()
    cutoff = calculator.calc(math, phy, chem)
    cutoff_label.config(text=f"Your cutoff is: {cutoff}")

    selected_course = course_var.get()

    selector = CourseSelection(cutoff, caste)
    selector.check()
    if not selector.is_eligible():
        messagebox.showwarning("Warning", "You are not eligible for admission in this college.")
        return

    selector.course_decide(selected_course)
    cour = selector.ret_cour()

    rno = random.randint(101, 399)
    create_database()
    insert_application(name, fname, age, cutoff, caste, cour, rno)

    with open("students.txt", "a") as f:
        f.write(f"\nName                   : {name}\n")
        f.write(f"Roll.No                : {rno}\n")
        f.write(f"Course                 : {cour}\n")

    if form_var.get() == 1:
        display_form(name, fname, age, cour, caste, cutoff)

    if view_list_var.get() == 1:
        with open("students.txt", "r") as f:
            students_list.delete(1.0, tk.END)
            students_list.insert(tk.END, f.read())

root = tk.Tk()
root.geometry("700x700")
root.title("PSG College of Technology Admission Form")
tk.Label(root,text="WELCOME TO PSG COLLEGE OF TECHNOLOGY",font=('Arial',22)).grid(row=0, columnspan=2, pady=10)
tk.Label(root, text="Enter your details below:").grid(row=1, columnspan=2, pady=10)

tk.Label(root, text="Name:").grid(row=2, column=0, sticky=tk.W, padx=10)
name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1, padx=10)

tk.Label(root, text="Father's Name:").grid(row=3, column=0, sticky=tk.W, padx=10)
fname_entry = tk.Entry(root)
fname_entry.grid(row=3, column=1, padx=10)

tk.Label(root, text="Age:").grid(row=4, column=0, sticky=tk.W, padx=10)
age_entry = tk.Entry(root)
age_entry.grid(row=4, column=1, padx=10)

tk.Label(root, text="Caste (OC/BC/SC):").grid(row=5, column=0, sticky=tk.W, padx=10)
caste_entry = tk.Entry(root)
caste_entry.grid(row=5, column=1, padx=10)

tk.Label(root, text="Maths Mark:").grid(row=6, column=0, sticky=tk.W, padx=10)
math_entry = tk.Entry(root)
math_entry.grid(row=6, column=1, padx=10)

tk.Label(root, text="Physics Mark:").grid(row=7, column=0, sticky=tk.W, padx=10)
phy_entry = tk.Entry(root)
phy_entry.grid(row=7, column=1, padx=10)

tk.Label(root, text="Chemistry Mark:").grid(row=8, column=0, sticky=tk.W, padx=10)
chem_entry = tk.Entry(root)
chem_entry.grid(row=8, column=1, padx=10)

tk.Label(root, text="Select Course:").grid(row=9, column=0, sticky=tk.W, padx=10)
course_var = tk.StringVar(root)
course_var.set("CSE")
course_options = ["CSE", "IT", "MECH", "CIVIL", "BM"]
course_menu = tk.OptionMenu(root, course_var, *course_options)
course_menu.grid(row=9, column=1, padx=10)

cutoff_label = tk.Label(root, text="")
cutoff_label.grid(row=10, columnspan=2, pady=10)

form_var = tk.IntVar()
tk.Checkbutton(root, text="Print Application Form", variable=form_var).grid(row=11, columnspan=2)

view_list_var = tk.IntVar()
tk.Checkbutton(root, text="View Students List", variable=view_list_var).grid(row=12, columnspan=2)

tk.Button(root, text="Submit", command=submit_form).grid(row=13, columnspan=2, pady=10)

students_list = tk.Text(root, height=12, width=70)
students_list.grid(row=14, columnspan=2, pady=10)

root.mainloop()


