import tkinter
import os
from tkinter import Tk, Entry, Button, Frame, LabelFrame, messagebox, Menu, Label, ttk, Spinbox, Checkbutton

# Functions

def enter_data():
    firstname = first_name_entry.get()
    number_inputs = 1
    list_first = []
    list_names = [firstname for _ in range(number_inputs)]

    with open(os.path.join("C:/Users/Pepito_Windows/Desktop/Hello_World/Tkinter/data_entry/informacion.txt"), "w") as arch:
        for name in list_names:
            arch.write(name + "\n")

# Root (Screen)

root = tkinter.Tk()
root.title("Data Entry")

frame = tkinter.Frame(root)
frame.pack()

# Save User Info

user_info_data = LabelFrame(frame, text= "Información de Usuario")
user_info_data.grid(row= 0, column= 0, padx= 20, pady= 10)

first_name_label = Label(user_info_data, text= "Nombre")
first_name_label.grid(row= 0, column= 0, padx=20, pady= 20)
last_name_label = Label(user_info_data, text= "Apellido")
last_name_label.grid(row= 0, column= 1, padx= 20, pady= 20)

first_name_entry = Entry(user_info_data)
last_name_entry = Entry(user_info_data)
first_name_entry.grid(row= 1, column= 0)
last_name_entry.grid(row= 1, column= 1)

title = Label(user_info_data, text= "Titulo")
title_combo = ttk.Combobox(user_info_data, values= ["", "Sr", "Sra"])
title.grid(row= 0, column= 2)
title_combo.grid(row= 1, column= 2)

age_label = Label(user_info_data, text= "Edad")
age_spin_box = Spinbox(user_info_data, from_= 18, to= 110)
age_label.grid(row= 2, column= 0)
age_spin_box.grid(row= 3, column= 0)

nationality_label = Label(user_info_data, text= "Nacionalidad")
nationality_combobox = ttk.Combobox(user_info_data, values= ["", "Venezuela", "Peru", "Colombia", "Argentina", "Panama", "Uruguay", "Guyana", "Ecuador", "Mexico", "Estado Unidos", "Hondura", "Cuba", "Bolivia", "Brazil", "Chile", "Costa Rica", "Puerto Rico", "Nicaragua", "Surinam", "Guyana Francesa", "Trinidad y Tobago", "Curazao", "Jaimaica", "Aruba", "Santa Lucia", "Republica Dominicana", "Barbados", "Granada", "Islas Turcas", "Islas Caiman", "Guatemala", "El Salvador"])
nationality_label.grid(row= 2, column= 1)
nationality_combobox.grid(row= 3, column = 1)

for widgets in user_info_data.winfo_children():
    widgets.grid_configure(padx= 10, pady= 5)

# Save Course Info

course_frame = LabelFrame(frame)
course_frame.grid(row= 1, column= 0, sticky= "news", padx= 20, pady= 10)

check_register_label = Label(course_frame, text= "Estado de registro")
check_register = Checkbutton(course_frame, text= "Actualmente registrado")

check_register_label.grid(row= 0, column= 0)
check_register.grid(row= 1, column= 0)

num_courses_label = Label(course_frame, text= "# Completar el numero de cursos")
num_courses_spin = Spinbox(course_frame, from_= 0, to= "infinity")

num_courses_label.grid(row= 0, column= 1)
num_courses_spin.grid(row= 1, column= 1)

num_semesters_label = Label(course_frame, text= "# Semestres")
num_semesters_spin = Spinbox(course_frame, from_= 0, to= "infinity")
num_semesters_label.grid(row= 0, column= 2)
num_semesters_spin.grid(row= 1, column= 2)

for widgets in course_frame.winfo_children():
    widgets.grid_configure(padx= 10, pady= 5)

# Terms & Condicion widget 
terms_frame = LabelFrame(frame, text= "Terminos y Condiciones")
terms_frame.grid(row= 2, column= 0, sticky="news", padx= 20, pady=10)

terms_check = Checkbutton(terms_frame, text= "Acepto terminos y condiciones")
terms_check.grid(row= 0, column= 0)

# Button check info

button = Button(frame, text= "Ingresar datos", command= enter_data)
button.grid(row= 3, column= 0, sticky="news", padx= 20, pady= 10)

root.mainloop()