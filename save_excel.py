import os
import openpyxl
import tkinter
from tkinter.filedialog import asksaveasfilename
from tkinter import Tk, ttk, Label, Frame, Button, LabelFrame, Entry, INSERT

def save_dir(screen):

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

    label_save = LabelFrame(frame, text= "Ruta del archivo")
    label_save.grid(row= 0, column= 0, pady= 20, padx= 10, sticky= "news")

    # Entry save

    entry_save_excel = Entry(label_save, width= 30)
    entry_save_excel.grid(row= 1, column=0, padx= 20, pady= 10)
    # Button save

    button_save_excel = Button(label_save, text= ".....", width= 3, command= save_xl)
    button_save_excel.grid(row= 1, column= 1, padx= 20, pady= 10)

    for widgets_save in label_save.winfo_children():
        widgets_save.grid_configure(padx= 10, pady= 5)

    return frame
    


