import tkinter

import openpyxl
from tkinter import Tk, Entry, Button, Frame, LabelFrame, messagebox, Label, ttk, Spinbox, Checkbutton, StringVar, Menu, PhotoImage
from Tkinter.Time_function.time_register_fun import time_register
from Tkinter.Excel_functions.save_excel import save_dir, dir_excel, get_file

# Root (Screen)

root = Tk()
root.title("Data Entry")
root.minsize(580, 480)

frame = Frame(root)
frame.pack()

# Icon App

icon_ = PhotoImage(file='logo.png')
root.iconphoto(False, icon_)

# Hide function
def hide_main_widget(widget):
    widget.pack_forget()

def show_main_widget(widget):
    widget.pack(fill="both", expand="YES")

# Menubar

def create_menu_bar(root, show_save):
    bmenu = Menu(root, background="#00ff00",
                 foreground="#ff0000",
                 activebackground="White",
                 activeforeground="Black")

    file_menu = Menu(bmenu, tearoff=0)
    file_menu.add_command(label="Agregar Datos", command=show_principal_frame)
    file_menu.add_command(label="Guardar", command=show_save)
    file_menu.add_command(label="Buscar Usuario", command=find_data)
    bmenu.add_cascade(label="Opciones", menu=file_menu)
    return bmenu

# Functions

def enter_data():
    """Retrieves user input from tkinter widgets, validate data(Optional), prompt for confirmations, and appends data to file.

    Raise:
        FileNotFoundError : If the especified file is not found.
        PermissionError : If the script lacks permission to write file to the file.
    """
    # Data collection from line 53 to line 66
    title_ = title_combo.get()
    firstname = first_name_entry.get()
    last_name = last_name_entry.get()
    nationality_ = nationality_combobox.get()
    age_ = age_spin_box.get()
    time_register_now = save_time_exactly()
    check_register_info = register_check_function.get()
    id_register = Id_entry.get()
    phone_number_data = phone_number_entry.get()
    email_data = email_entry.get()
    num_courses = num_courses_spin.get()
    num_semesters_spin_data = num_semesters_spin.get()
    terms_data_check = terms_check_var.get()

    # Work on Excel File

    file_dir = get_file()

    work_excel = openpyxl.load_workbook(file_dir)
    sheet_excel = work_excel.active
    sheet_excel.append([id_register, title_, firstname, last_name, age_, nationality_,
                        check_register_info, num_courses, num_semesters_spin_data, terms_data_check,
                        phone_number_data, email_data, time_register_now])
    work_excel.save(file_dir)
    return enter_data

# Find data & return

def find_data():
    pass

# Direction Excel & Save file

def dir_excel_file():
    dir_str = dir_excel()
    return dir_str

# Saved exactly time

def save_time_exactly():
    save_time_exactly_v = time_register()
    return save_time_exactly_v

# Term and condictions text info widget

def term_cond_text_info():
    term_conds_text = messagebox.showinfo(title="Tèrminos y Condiciones", message="Ser mayor de 18 años")
    return term_conds_text


# Screen Save Excel files

frame_save = save_dir(root)

def show_save():
    show_main_widget(frame_save)
    frame.pack_forget()

def show_principal_frame():
    show_main_widget(frame)
    frame_save.pack_forget()

# Save User Info

user_info_data = LabelFrame(frame, text="Información de Usuario")
user_info_data.grid(row=0, column=0, padx=20, pady=10, sticky="news")

first_name_label = Label(user_info_data, text="Nombre")
first_name_label.grid(row=0, column=0, padx=20, pady=20)
last_name_label = Label(user_info_data, text="Apellido")
last_name_label.grid(row=0, column=1, padx=20, pady=20)

first_name_entry = Entry(user_info_data, width=24)
last_name_entry = Entry(user_info_data, width=24)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title = Label(user_info_data, text="Titulo")
title_combo = ttk.Combobox(user_info_data, values=["", "Sr", "Sra"], width=20)
title.grid(row=0, column=2)
title_combo.grid(row=1, column=2)

age_label = Label(user_info_data, text="Edad")
age_spin_box = Spinbox(user_info_data, from_=18, to=110, width=23)
age_label.grid(row=2, column=0)
age_spin_box.grid(row=3, column=0)

nationality_label = Label(user_info_data, text="Nacionalidad")
nationality_combobox = ttk.Combobox(user_info_data,
                                    values=["", "Venezuela", "Peru", "Colombia", "Argentina", "Panama", "Uruguay",
                                            "Guyana", "Ecuador", "Mexico", "Estado Unidos", "Hondura", "Cuba",
                                            "Bolivia", "Brazil", "Chile", "Costa Rica", "Puerto Rico", "Nicaragua",
                                            "Surinam", "Guyana Francesa", "Trinidad y Tobago", "Curazao", "Jaimaica",
                                            "Aruba", "Santa Lucia", "Republica Dominicana", "Barbados", "Granada",
                                            "Islas Turcas", "Islas Caiman", "Guatemala", "El Salvador"], width=20)
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

Id_Label = Label(user_info_data, text="ID")
Id_entry = Entry(user_info_data, width=24)
Id_Label.grid(row=2, column=2, padx=20, pady=10)
Id_entry.grid(row=3, column=2)

phone_number_label = Label(user_info_data, text="Telefono")
phone_number_entry = Entry(user_info_data, width=24)
phone_number_label.grid(row=4, column=0, padx=20, pady=10)
phone_number_entry.grid(row=5, column=0)

email_label = Label(user_info_data, text="Correo Electronico")
email_entry = Entry(user_info_data, width=24)
email_label.grid(row=4, column=1, padx=20, pady=10)
email_entry.grid(row=5, column=1)

find_user = Button(user_info_data,text="Buscar Usuario", command=find_data)
find_user.grid_configure(row=4, column=2, rowspan=2, sticky="news", ipady= 10)

for widgets in user_info_data.winfo_children():
    widgets.grid_configure(padx=10, pady=5)

# Save Course Info

course_frame = LabelFrame(frame, text="Estado de registro")
course_frame.grid_configure(row=1, column=0, sticky="news", padx=20, pady=10)
course_frame.columnconfigure(0, weight=3)

register_check_function = StringVar(value="No")
check_register = Checkbutton(course_frame, text="Actualmente registrado", variable=register_check_function,
                             onvalue="Si", offvalue="No")
check_register.grid_configure(row=0, column=0, rowspan=2)

num_courses_label = Label(course_frame, text="Cursos completados")
num_courses_spin = Spinbox(course_frame, from_=0, to="infinity")

num_courses_label.grid(row=0, column=1)
num_courses_spin.grid(row=1, column=1)

num_semesters_label = Label(course_frame, text= "Semestres")
num_semesters_spin = Spinbox(course_frame, from_=0, to="infinity")
num_semesters_label.grid(row=0, column=2)
num_semesters_spin.grid(row=1, column=2)

for widgets in course_frame.winfo_children():
    widgets.grid_configure(padx=6, pady=10)

# Terms & Condicion widget 
terms_frame = LabelFrame(frame, text="Terminos y Condiciones")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check_var = StringVar(value="No")
terms_check = Checkbutton(terms_frame, text="Acepto terminos y condiciones", variable=terms_check_var, onvalue="Si",
                          offvalue="No")
terms_check.grid(row=0, column=0)

# Term and condictions text

terms_text = Button(terms_frame, text="Ver", width=4, height=1, command=term_cond_text_info)
terms_text.grid(row=0, column=3, sticky="news", padx=20, pady=20)

# Button check info

button_term_tex = Button(frame, text="Ingresar datos", command=enter_data)
button_term_tex.grid(rowspan=1, column=0, sticky="news", padx=20, pady=10)

root.config(menu=create_menu_bar(root, show_save))
root.mainloop()
