from tkinter import *

raiz = Tk()

# Sirve para redimecionar la ventana
# raiz.resizable(True, False)

# Se le da un nombre al titulo
raiz.title = "Venatana de pruebas"
# Se le da el tamaño a la ventana
# raiz.geometry('650x350')
# La raiz se adapata al tamaño de los frames
raiz.config(bg="blue")
# Creamos el frame

miFrame = Frame()
# Empaquetamos el frame

miFrame.config(width="650", height="350")
miFrame.config(bg="red")
miFrame.pack()
# Pega el frame a donde se indique con el metodo side
# miFrame.pack(side="left", anchor="n")
# miFrame.pack(fill="x")
# Rellena de forma horizonal
# miFrame.pack(fill="y", expand="True")
# Rellena en el eje de las YS
# miFrame.pack(fill="both", expand="True")
# Expande en los 2 ejes
# Da unborde 
miFrame.config(bd=35)
miFrame.config(relief="groove")

# miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")
# pone el cursor en pointer
raiz.mainloop()