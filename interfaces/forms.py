#  el input se llama entry en tkinter

from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=500)
miFrame.pack()

cuadroTexto = Entry( miFrame )
cuadroTexto.place(x=100, y=200)

raiz.mainloop()