from cliente import *

#Data Class: It helps to make a better use and more ordered use of the information you can get from the server.
class Data:
    def __init__(self):
        self.ID = []         #List of Process ID
        self.Strings = []    #List of Strings, it is in the same order than Process ID list
        self.Length = 0      #Integer which returns the length of both lists
        self.updateData()    
        
    #updateData Method: Update the information of Data class, is used after add or remove data from the server in the interface
    def updateData(self):
        opciones = showDeleteOptions()
        self.ID = opciones[0]
        self.Strings = opciones[1]
        self.Length = len(self.ID)
        return

    #getLength Method: Returns the length of the vectors mentioned above
    def getLength(self):
        return self.Length
