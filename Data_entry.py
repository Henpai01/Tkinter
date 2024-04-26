import tkinter
import openpyxl
from tkinter import Tk, Entry, Button, Frame, LabelFrame, messagebox, Label, ttk, Spinbox, Checkbutton, StringVar, Menu
from time_register_fun import time_register
from save_excel import save_dir

# Root (Screen)

root = tkinter.Tk()
root.title("Data Entry")
root.minsize(580, 480)

frame = tkinter.Frame(root)
frame.pack()

# Hide function

def hide_main_widget(widget):
    widget.pack_forget()

def show_main_widget(widget): 
    widget.pack(fill= "both", expand= "YES") 


# Menubar

def create_menu_bar(root, show_save):
    bmenu = Menu(root, background="#00ff00",
                 foreground="#ff0000",
                 activebackground="White",
                 activeforeground="Black")

    file_menu = Menu(bmenu, tearoff= 0)
    file_menu.add_command(label = "Agregar Datos", command = show_principal_frame)
    file_menu.add_command(label = "Guardar ", command = show_save)
    bmenu.add_cascade(label= "Opciones", menu = file_menu)
    return bmenu


# Functions

def enter_data():
    """Retrieves user input from tkinter widgets, validate data(Optional), prompt for confirmations, and appends data to file.

    Raise:
        FileNotFoundError : If the especified file is not found.
        PermissionError : If the script lacks permission to write file to the file.
    """
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
    number_inputs = 1
    list_first = []
    list_names = [firstname for _ in range(number_inputs)]



# Saved exactly time

def save_time_exactly():
    save_time_exactly_v = time_register()
    return save_time_exactly_v

# Term and condictions text info widget

def term_cond_text_info():
    term_conds_text = messagebox.showinfo(title= "Tèrminos y Condiciones", message="Ser mayor de 18 años")
    return term_conds_text

# Screen Save

frame_save = save_dir(root)

def show_save():
    show_main_widget(frame_save)
    frame.pack_forget()

def show_principal_frame():
    show_main_widget(frame)
    frame_save.pack_forget()

# Save User Info

user_info_data = LabelFrame(frame, text= "Información de Usuario")
user_info_data.grid(row= 0, column= 0, padx= 20, pady= 10, sticky= "news")

first_name_label = Label(user_info_data, text= "Nombre")
first_name_label.grid(row= 0, column= 0, padx=20, pady= 20)
last_name_label = Label(user_info_data, text= "Apellido")
last_name_label.grid(row= 0, column= 1, padx= 20, pady= 20)

first_name_entry = Entry(user_info_data, width= 20)
last_name_entry = Entry(user_info_data, width= 20)
first_name_entry.grid(row= 1, column= 0)
last_name_entry.grid(row= 1, column= 1)

title = Label(user_info_data, text= "Titulo")
title_combo = ttk.Combobox(user_info_data, values= ["", "Sr", "Sra"], width= 20)
title.grid(row= 0, column= 2)
title_combo.grid(row= 1, column= 2)

age_label = Label(user_info_data, text= "Edad")
age_spin_box = Spinbox(user_info_data, from_= 18, to= 110, width= 20)
age_label.grid(row= 2, column= 0)
age_spin_box.grid(row= 3, column= 0)

nationality_label = Label(user_info_data, text= "Nacionalidad")
nationality_combobox = ttk.Combobox(user_info_data, values= ["", "Venezuela", "Peru", "Colombia", "Argentina", "Panama", "Uruguay", "Guyana", "Ecuador", "Mexico", "Estado Unidos", "Hondura", "Cuba", "Bolivia", "Brazil", "Chile", "Costa Rica", "Puerto Rico", "Nicaragua", "Surinam", "Guyana Francesa", "Trinidad y Tobago", "Curazao", "Jaimaica", "Aruba", "Santa Lucia", "Republica Dominicana", "Barbados", "Granada", "Islas Turcas", "Islas Caiman", "Guatemala", "El Salvador"], width= 20)
nationality_label.grid(row= 2, column= 1)
nationality_combobox.grid(row= 3, column = 1)

Id_Label = Label(user_info_data, text= "ID")
Id_entry = Entry(user_info_data, width= 20)
Id_Label.grid(row= 2, column= 2, padx= 20, pady= 10) 
Id_entry.grid(row= 3, column= 2)

phone_number_label = Label(user_info_data, text= "Telefono")
phone_number_entry = Entry(user_info_data, width= 20)
phone_number_label.grid(row= 4, column= 0, padx=20, pady=10)
phone_number_entry.grid(row= 5, column= 0)

email_label = Label(user_info_data, text= "Correo Electronico")
email_entry = Entry(user_info_data, width= 20)
email_label.grid(row= 4, column= 1, padx= 20, pady= 10)
email_entry.grid(row= 5, column= 1)

for widgets in user_info_data.winfo_children():
    widgets.grid_configure(padx= 10, pady= 5)

# Save Course Info

course_frame = LabelFrame(frame)
course_frame.grid(row= 1, column= 0, sticky= "news", padx= 20, pady= 10)

check_register_label = Label(course_frame, text= "Estado de registro")

register_check_function = StringVar(value="No")
check_register = Checkbutton(course_frame, text= "Actualmente registrado", variable= register_check_function, onvalue= "Si", offvalue= "No")

check_register_label.grid(row= 0, column= 0)
check_register.grid(row= 1, column= 0)

num_courses_label = Label(course_frame, text= "Numero de cursos completados")
num_courses_spin = Spinbox(course_frame, from_= 0, to= "infinity")

num_courses_label.grid(row= 0, column= 1)
num_courses_spin.grid(row= 1, column= 1)

num_semesters_label = Label(course_frame, text= "Semestres")
num_semesters_spin = Spinbox(course_frame, from_= 0, to= "infinity")
num_semesters_label.grid(row= 0, column= 2)
num_semesters_spin.grid(row= 1, column= 2)

for widgets in course_frame.winfo_children():
    widgets.grid_configure(padx= 10, pady= 5)

# Terms & Condicion widget 
terms_frame = LabelFrame(frame, text= "Terminos y Condiciones")
terms_frame.grid(row= 2, column= 0, sticky="news", padx= 20, pady= 10)

terms_check_var = StringVar(value= "No")
terms_check = Checkbutton(terms_frame, text= "Acepto terminos y condiciones", variable= terms_check_var, onvalue= "Si", offvalue= "No")
terms_check.grid(row= 0, column= 0)

# Term and condictions text

terms_text = Button(terms_frame, text="Ver", width= 4, height= 1, command= term_cond_text_info)
terms_text.grid(row= 0, column= 3, sticky="news", padx= 20, pady= 20)

# Button check info

button_term_tex = Button(frame, text= "Ingresar datos", command= enter_data)
button_term_tex.grid(rowspan= 1, column= 0, sticky="news", padx= 20, pady= 10)

root.config(menu=create_menu_bar(root, show_save))
root.mainloop()