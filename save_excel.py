import os
import openpyxl
import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import Tk, ttk, Label, Frame, Button, LabelFrame, Entry, INSERT

def save_dir(screen):

    def dir_excel():
        direction = askopenfilename()
        return str(direction)

    frame = Frame(screen)

    def save_xl():
        
        files = [('Excel', '*.xlsx')] 
        file_excel = asksaveasfilename(filetypes = files, defaultextension = files)


        if file_excel:
            work_book_excel = openpyxl.Workbook()
            sheet = work_book_excel.active
            
            # Cells width
            
            columns_width = ['C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
            new_width = 24

            for col in columns_width:
                sheet.column_dimensions[col].width = new_width
            
            # Heading Cells
            
            heading = ["ID", "Titulo", "Nombre", "Apellido", "Edad", "Pais",
                        "Registrado", "Semestres", "Numero de Semetres",
                        "Terminos & Condiciones", "Numero de Telefono", "Email",
                        "Tiempo"]
            sheet.append(heading)
            work_book_excel.save(file_excel)

            return file_excel
        else:
            return None

    # Label 

    label_save = LabelFrame(frame, text= "Ruta para crear y guardar el archivo")
    label_save.grid(row= 0, column= 0, pady= 20, padx= 10, sticky= "news")

    # Button save

    button_save_excel = Button(label_save, text= "Crear un nuevo archivo", width= 18, command= save_xl)
    button_save_excel.grid(row= 0, column= 0, padx= 20, pady= 10)

    # Label text

    save_label_text = Label(label_save, text= "será archivo Excel.")
    save_label_text.grid(row= 0, column= 1)

    for widgets_save in label_save.winfo_children():
        widgets_save.grid_configure(padx= 10, pady= 5)

    # Label for save

    label_dir = LabelFrame(frame, text= "Buscar ruta del archivo")
    label_dir.grid(row= 1, column= 0, pady= 15, padx= 10, sticky= "news")

    # Dir save

    entry_dir_save = Entry(label_dir)
    entry_dir_save.insert(0, dir_excel)
    entry_dir_save.grid(row=0, column=0, padx=20, pady=10)

    button_look_save = Button(label_dir, text="Buscar ruta del archivo", command= dir_excel)
    button_look_save.grid(row=0, column=1, padx=20, pady=10)

    for widgets_save in label_dir.winfo_children():
        widgets_save.grid_configure(padx= 10, pady= 5)

    return frame
    


