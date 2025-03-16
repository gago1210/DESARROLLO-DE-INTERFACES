import tkinter as tk  # le doy un nombre

from tkinter import ttk
from tkinter import * #importo la generalidad de la libreria

def altas():
    # funciones de cálculo u operativa, y otras ventanas superiores
    #cogiendo el objeto definido abajo previamente, damos configuracion a su ventana correspondiente, asi en todos los casos
    altas = tk.Toplevel()
    altas.title("Ventana altas")
    altas.geometry("300x300+400+400")
    altas.configure(bd=20)
    altas.resizable(False,False)

    Label(altas,text="Ventana superior").grid(row=2,column=2,padx=10,pady=10)

    altas.mainloop()


def bajas():
    # Funciones para la ventana de bajas
    def sumar():
        res.set(float(num1.get()) + float(num2.get()))

    def resta():
        res.set(float(num1.get()) - float(num2.get()))

    def multi():
        res.set(float(num1.get()) * float(num2.get()))

    def borrar():
        num1.set("")
        num2.set("")
        res.set("")

    def creditos():
        creditos = tk.Toplevel()

        creditos.mainloop()

    # Crear la ventana de bajas
    bajas = tk.Toplevel()
    bajas.title("Bajas")
    bajas.configure(bd=20)
    bajas.resizable(width=False, height=False)

    # Variables de ventana
    num1 = StringVar()
    num2 = StringVar()
    res = StringVar()

    # Etiquetas y inputs

    Label(bajas,text="Primer número").pack()
    Entry(bajas,justify="center",textvariable=num1).pack() # Primer número de la operación

    Label(bajas,text="Segundo número").pack()
    Entry(bajas,justify="center",textvariable=num2).pack() # Segundo número de la operación

    Label(bajas,text="Resultado").pack()
    Entry(bajas,justify="center",textvariable=res,state="disabled").pack()

    Label(bajas,text="").pack() # Espacio de separación de botones

    Button(bajas, text="Sumar", command=sumar).pack(side="left")
    Button(bajas, text="Restar", command=resta).pack(side="left")
    Button(bajas, text="Multiplicar", command=multi).pack(side="left")
    Button(bajas, text="Borrar", command=borrar).pack(side="left")
    Button(bajas, text="Altas", command=creditos).pack(side="left")
    bajas.mainloop()

#creo la ventana principal (con tk). Aclaración: al estar en la ventana principal, es la ventana que va a tener dentro el resto de ventanas 
#pequeñas (arriba escritas e identadas), tambien puedo tener funciones que sean ventanas a las que pueda llamar. La ventana principal
#siempre va a ser la general, la que voy a generar con el tk;

#inicio del bucle de ventana principal
principal = tk.Tk() # Creación del Objeto ventana
principal.title("Ventana principal de ejemplo") #ficheros de texto,bbdd
principal.geometry("600x400+300+300") #tamaño definido y maximo de la ventana 
principal.minsize(400,300) #tamaño minimo de la ventana
principal.configure(bd=20, background="ligthblue") #configuracion principal, ponemos la que mas se usa bd=20
principal.resizable(False,False) 

#hacemos unos marcos para la ventana
marco = ttk.Frame(principal) #hacemos un frame. esto es para meter el frame dentro de principal, creamos como un objeto.
marco.pack(expand=True) #pack para agrupar cosas, para que se adapte lo que tenga dentro

#hacemos una serie de botones:
boton1 = ttk.Button(marco, text="ALTAS", command=altas) #creamos el contenido (ttk.Button(marco, text="ALTAS", command=altas) asignandole un objeto (botonX)
boton1.grid(row=0,column=0,padx=5,pady=5) #creamos una rejilla para colocarlo

boton2 = ttk.Button(marco, text="BAJAS", command=bajas)
boton2.grid(row=0,column=1,padx=5,pady=5)

boton3 = ttk.Button(marco, text="INFORMES")
boton3.grid(row=1,column=0,padx=5,pady=5)

boton4 = ttk.Button(marco, text="CONTRATOS")
boton4.grid(row=1,column=1,padx=5,pady=5)

principal.mainloop() # Bucle principal de ventana. Aqui acaba el bucle principal que nos crea la ventana donde despues va a encontrarse el 
#resto de las ventanas.