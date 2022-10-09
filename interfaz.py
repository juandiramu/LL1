from tkinter import *

raiz= Tk()
raiz.title("Interfaz LL1")
raiz.resizable(1,1)
#raiz.geometry("1000x1000")
raiz.config(bg="white")

#frame=Frame()
#frame.pack()
#frame.config(bg="gray")
#frame.config(width="1450",height="1000")

def enviarDatos():
    mensaje = mensajeTxt.get(1.0, "end-1c")
    print(mensaje)
    raiz.destroy()

Label(text="Cadena a evaluar", fg='Black', font=("Black", 12)).grid(row=0, column=0, sticky="e", padx=50, pady=10)
mensajeTxt = Text(raiz, width=180 , height=180 )
mensajeTxt.grid(row=1, column=0)

botonEnviar = Button(raiz, text="Aceptar", fg="black", font=("Verdana",14), command=enviarDatos)
botonEnviar.grid(row=7, column=0, padx=20, pady=20)

#Siempre dejar al final
raiz.mainloop()