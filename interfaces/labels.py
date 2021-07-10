from  tkinter import *

root = Tk()

miFrame = Frame(root, width=400, height=500)

miFrame.pack()

Label(miFrame, text="Hola mundo", fg="blue", font=("Comic Sans MS", 24)).place(x=100, y=200)
# perimte ubicar el texto dentro de las coordenadas X y Y


root.mainloop()
