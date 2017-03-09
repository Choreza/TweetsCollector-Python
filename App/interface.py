import Tkinter as tk
from Tkinter import *
import ttk
from tkSearch import *
from tkDelete import *

#Strings used below to assign name of the tabs
b = "Busqueda"
t1 = "Keyword"
t2 = "Usuario"
t3 = "Procesos"
processes = []

#TwitterApp Class: This is the main window of our application and is used to manage a great part of the program
class TwitterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.topLabel = tk.Label(self, text = "Twitter App")       #Title of the window
        self.topLabel.pack()

        self.tab = ttk.Notebook(self)                              #Tabs interface
        
        titles = [b, t3]                                           #Titles of the tabs
        self.frames = {}                                           #Frames for use the tabs
        for title in titles:
            self.frames[title] = ttk.Frame(self.tab)
            self.tab.add(self.frames[title], text = title)

        self.searchKey = toSearch(self.frames[b], b, self)         #Search Frame
        self.searchKey.pack()

        #Frame for list of processes
        self.deleteList = toDelete(self.frames[t3], self)          #Delete List Frame
        self.deleteList.pack()
        
        self.tab.pack()
        

app = TwitterApp()

#Title of the program
app.title("Twitter App")

#Set window size here
app.geometry('565x380')                               
app.mainloop()
