import Tkinter as tk
from Tkinter import *
import ttk
import cliente as cli

b = "Busqueda por "
t1 = "Keyword"
t2 = "Usuario"
t3 = "Eliminar Proceso"
processes = []

#toSearch Class: Search interface
class toSearch(ttk.Frame):
    def __init__(self, parent, searchType, controller):
        ttk.Frame.__init__(self, parent)

        self.controller = controller
        
        #Interface stuff
        self.toSearch = ttk.Label(self, text = searchType, justify = LEFT)
        self.toSearch.grid(row = 0, column = 0, padx = 30, pady = 10, sticky = "W")

        self.Field = ttk.Entry(self, width = 34)
        self.Field.grid(row = 0, column = 2, columnspan = 2)

        self.totalTime = ttk.Label(self, text = "Tiempo Total")
        self.totalTime.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = "W")

        self.tField = ttk.Entry(self)
        self.tField.grid(row = 1, column = 2)

        self.var = tk.StringVar()
        self.tlist = ttk.Combobox(self, textvariable = self.var,
                                  values = ["Semanas", "Indefinido"],
                                  state = "readonly")
        self.tlist.current(1)
        self.tlist.configure(width = 9)
        self.tlist.grid(row = 1, column = 3, padx = 5)

        self.fileName = ttk.Label(self, text = "Nombre del Archivo")
        self.fileName.grid(row = 2, column = 0, padx = 30, pady = 10)

        self.fileField = ttk.Entry(self, width = 34)
        self.fileField.grid(row = 2, column = 2, columnspan = 2)

        self.start = ttk.Button(self,
                                text = "Comenzar",
                                command = self.searchCommand)
        self.start.grid(row = 3, column = 3)
        self.var.trace("w", self.on_trace_choice)
        self.refresh()
    
    #searchCommand Method: Is used after click the "Buscar" button
    def searchCommand(self):
        String = self.Field.get() #String a buscar
        totalTime = self.tField.get()
        typeTime = self.tlist.get() #Puede ser "Semanas" o "Indefinido"
        fileName = self.fileField.get() #Nombre del archivo
        
        if typeTime == "Indefinido":
            totalTime = -1
            
        asd = cli.search(String, totalTime, fileName)
        self.searchRefresh()
        self.controller.deleteList.updateWindow()
        return
    
    #on_trace_choice Method: Update the checkboxes
    def on_trace_choice(self, name, index, mode):
        self.refresh()
      
    #refresh Method: Updates the checkboxes according to the selected search type
    def refresh(self):
        typeTime = self.tlist.get()
        if typeTime == "Indefinido":
            self.tField.delete(0, "end")
            self.tField.configure(state = "disabled")
        else:
            self.tField.configure(state = "normal")
        return
    
    #searchRefresh Method: Updates the window before click the "Buscar" button
    def searchRefresh(self):
        self.tlist.current(1)
        self.Field.delete(0, "end")
        self.tField.delete(0, "end")
        self.fileField.delete(0, "end")
        return
