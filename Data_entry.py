import tkinter
import os
import datetime
import time 
from tkinter import Tk, Entry, Button, Frame, LabelFrame, messagebox, Menu, Label, ttk, Spinbox, Checkbutton

# Functions

def enter_data():
    """Retrieves user input from tkinter widgets, validate data(Optional), prompt for confirmation, and appends data to file.

    Raise:
        FileNotFoundError : If the especified file is not found.
        PermissionError : If the script lacks permission to write file to the file.
    """
    nationality_ = nationality_combobox.get()
    age_ = age_spin_box.get()
    title_ = title_combo.get()
    last_name = last_name_entry.get()
    firstname = first_name_entry.get()
    time_register_now = time_register()
    check_register_info = check_info_data()
    id_register = Id_entry.get()
    number_inputs = 1
    list_first = []
    list_names = [firstname for _ in range(number_inputs)]

    
    with open(os.path.join("C:/Users/Pepito_Windows/Desktop/Hello_World/Tkinter/data_entry/informacion.txt"), "a") as arch:
        for data_ in list_names:
            arch.write(f"ID: {id_register}, {title_} {firstname} {last_name}, Edad: {age_}, Pais: {nationality_}, Registrado: {check_register_info}, Hora:{time_register_now}" + "\n")

            # validate inputs types (adjust as needed)
            try:
                int(age_)
            except ValueError_:
                messagebox.showerror(title="Coloca un número valido!", message="Intenta nuevamente.")
                continue

# Saved exactly time
def time_register():
    current_time = time.time()
    time_object = datetime.datetime.fromtimestamp(current_time)
    formatted_time = time_object.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

# Term and condictions text info widget

def term_cond_text_info():
    Term_conds_text = messagebox.showinfo(title= "Tèrminos y Condiciones", message="Ser mayor de 18 años")
    return Term_conds_text

# check info

def check_info_data():
    if check_register == True:
        return ("Sí") 
    else:
        return ("No")

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

Id_Label = Label(user_info_data, text= "ID")
Id_entry = Entry(user_info_data)
Id_Label.grid(row= 2, column= 2, padx= 20, pady= 10) 
Id_entry.grid(row= 3, column= 2)

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

# Term and condictions text

terms_text = Button(terms_frame, text="Ver", width= 4, height= 1, command= term_cond_text_info)
terms_text.grid(row= 0, column= 3, sticky="news", padx= 20, pady= 20)

# Button check info

button_term_tex = Button(frame, text= "Ingresar datos", command= enter_data)
button_term_tex.grid(rowspan= 1, column= 0, sticky="news", padx= 20, pady= 10)


root.mainloop()