import tkinter
from tkinter import Tk, Entry, Button, Frame, LabelFrame, messagebox, Menu, Label, ttk, Spinbox

# Root (Screen)

root = tkinter.Tk()
root.title("Data Entry")
root.geometry("400x380")

frame = tkinter.Frame(root)
frame.pack()

# Save User Info

user_info_data = LabelFrame(frame, text= "Información de Usuario")
user_info_data.grid(row= 0, column= 0)

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

root.mainloop()