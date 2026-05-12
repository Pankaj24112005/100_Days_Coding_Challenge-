import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook


# ======================================================
# DATA STORAGE (MODEL / BUSINESS LOGIC)
# ======================================================
# Dictionary acts as in-memory database for students
student_grades = {}


# ======================================================
# CORE FUNCTIONS (CRUD OPERATIONS)
# ======================================================
# These functions contain only logic, no GUI code

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")
    else:
        print(f"{name} is not found!")

def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No student found/added")


# ======================================================
# GUI CONTROLLER FUNCTIONS (CONNECT GUI ↔ LOGIC)
# ======================================================
# These functions take input from GUI and call core logic

def gui_add_student():
    if name_entry.get() and grade_entry.get():
        add_student(name_entry.get(), int(grade_entry.get()))
        refresh_display()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter name and grade")

def gui_update_student():
    if name_entry.get() and grade_entry.get():
        update_student(name_entry.get(), int(grade_entry.get()))
        refresh_display()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter name and grade")

def gui_delete_student():
    if name_entry.get():
        delete_student(name_entry.get())
        refresh_display()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter student name")

# Update text area with current student data
def refresh_display():
    # Clear previous content
    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)

    # Show current student data
    if student_grades:
        for name, grade in student_grades.items():
            output_box.insert(tk.END, f"• {name} : {grade}\n")
    else:
        output_box.insert(tk.END, "No student found")

    # Lock text box to read-only
    output_box.config(state="disabled")


# Clear input fields after each operation
def clear_entries():
    name_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

# ======================================================
# FILE DOWNLOAD FUNCTION (EXPORT TO EXCEL)
# ======================================================
# Converts student_grades dictionary into Excel file

def download_excel():
    if not student_grades:
        messagebox.showwarning("No Data", "No student records to download")
        return

    # Create a new Excel workbook and sheet
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Student Grades"

    # Add header row
    sheet.append(["Student Name", "Grade"])

    # Add student data rows
    for name, grade in student_grades.items():
        sheet.append([name, grade])

    # Save file
    file_name = "student_grades.xlsx"
    wb.save(file_name)

    messagebox.showinfo("Success", f"Data downloaded as {file_name}")



# ======================================================
# GUI SETUP (VIEW LAYER)
# ======================================================
# Main application window
root = tk.Tk()
root.title("Student Grades Management")
root.geometry("450x520")
root.configure(bg="#1e1e2f")

# ======================================================
# UI STYLING (COLORS & FONTS)
# ======================================================
TITLE_FONT = ("Segoe UI", 18, "bold")
LABEL_FONT = ("Segoe UI", 11)
BTN_FONT = ("Segoe UI", 10, "bold")

BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2a2a40"
BTN_COLOR = "#4CAF50"
BTN_HOVER = "#43a047"
TEXT_COLOR = "#ffffff"

# ======================================================
# CARD LAYOUT (MODERN UI DESIGN)
# ======================================================
# Card frame gives clean and centered look
card = tk.Frame(root, bg=CARD_COLOR)
card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=480)

# ======================================================
# UI COMPONENTS (INPUTS)
# ======================================================
tk.Label(card, text="Student Grades System",
         font=TITLE_FONT, fg=TEXT_COLOR, bg=CARD_COLOR).pack(pady=15)

tk.Label(card, text="Student Name",
         font=LABEL_FONT, fg=TEXT_COLOR, bg=CARD_COLOR).pack()
name_entry = tk.Entry(card, width=30, font=LABEL_FONT)
name_entry.pack(pady=5)

tk.Label(card, text="Student Grade",
         font=LABEL_FONT, fg=TEXT_COLOR, bg=CARD_COLOR).pack()
grade_entry = tk.Entry(card, width=30, font=LABEL_FONT)
grade_entry.pack(pady=5)


# ======================================================
# BUTTON STYLING WITH HOVER EFFECT
# ======================================================
def on_enter(e):
    e.widget["background"] = BTN_HOVER

def on_leave(e):
    e.widget["background"] = BTN_COLOR

def styled_button(text, command):
    btn = tk.Button(card, text=text, command=command,
                    bg=BTN_COLOR, fg="white",
                    font=BTN_FONT, width=22, bd=0)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=5)
    return btn

# Action buttons
styled_button("Add Student", gui_add_student)
styled_button("Update Student", gui_update_student)
styled_button("Delete Student", gui_delete_student)
styled_button("View Students", refresh_display)
styled_button("Download File", download_excel)


# ======================================================
# OUTPUT DISPLAY AREA
# ======================================================
# Text widget used to display student records
output_box = tk.Text(card, height=8, width=38,
                     font=("Consolas", 10),
                     bg="#12121c", fg="white", bd=0)
output_box.pack(pady=10)


# ======================================================
# START GUI EVENT LOOP
# ======================================================
root.mainloop()
