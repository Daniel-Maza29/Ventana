import tkinter as tk
#from tkinter import * 
from PIL import Image, ImageTk # instalar Pillow

ventana = tk.Tk()
# agregando icono de la ventana 

#path = Image.open("C:\Users\Biblioteca\Desktop\ventana\descarga.jpg")
#icono = ImageTk.PhotoImage(path)
#ventana.iconphoto(True, icono)

#establecemos el nombre del titulo de la ventana 
ventana.title("Daniel APP")

# Establecemos el tamaño de la ventana. ventana.geometry("<ancho>x<alto>+<posición_x>+<posición_y>")

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Establecer el tamaño completo de la ventana
ventana.geometry(f"{1024}x{900}")

# Definimos si la ventana puede ser modificada en su tamaño.
ventana.resizable(True, True) 

# Podemos añadir configuraciones adicionales a la ventana con la funcion config
ventana.config(bg="gray")


# inicializamos la aplicacion 

etiqueta = tk.Label(ventana, text="HOLAAA!!!!!\n ESTOY AQUÍ!!!")
etiqueta.pack()

#EMPECEMOS A PERSONALIZAR
etiqueta = tk.Label(ventana, text="HOLAAA, ESTOY AQUI!!", bg="red", fg="blue", font=("Time New Roman", 16), width=20, height=2, anchor="center")
etiqueta.pack()

#button

def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado!")

etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

def cambiar_texto():
    etiqueta.config(text="¡HAZ CAMBIADO EL TEXTO!")

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Preciona para cambiar texto")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Time New Roman", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

# Crear un marco con borde sólido
marco1 = tk.Frame(ventana, width=400, height=300, bd=2, relief="solid")
marco1.pack()

# Agregar una etiqueta al marco1
etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()

#frame
# Crear un marco con borde en relieve
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

# Agregar una etiqueta al marco2
etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)


#checkbutton
cuadro_lista = tk.Listbox(ventana, width=30, selectmode="single")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")



variable = tk.IntVar()

casilla_verificacion = tk.Checkbutton(ventana, text="Unica opcion 1", variable=variable, command=obtener_estado)
casilla_verificacion.pack()
# Radiobutton
def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")



variable = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="Opción 1", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="Opción 2", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="Opción 3", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()

#posicionar los widgest
#place 

from tkinter import * 

master = Tk()
master.geometry("800x600")

# Creacion de labels
l1 = Label(master, text = "Nombre:")
l2 = Label(master, text = "Apellido:")

#Definiendo posiciones 
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# Creando cajas de texto con Entry
nombre = Entry(master)
apellido = Entry(master)

# Definiendo posisicones para cajas de texto
nombre.grid(row = 0, column = 1, pady = 4)
apellido.grid(row = 1, column = 1, pady = 4)

ventana.mainloop()



#DANIEL RAFAEL MAZA RUIZ