from Tkinter import *

class Interface:
    def __init__(self, container):
        self.e1 = Label (container.text = "Label 1", fg = "black", bg = "white")
        self.e1.pack()


window = Tk()
myInterface = Interface(window)
window.mainloop()


