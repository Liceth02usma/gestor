# Para este proyecto se utilizara la libreria TKinter
import tkinter 

# Ventana en la que se mostraran todos los elementos graficos
windows = tkinter.Tk()
windows.geometry("400x300") #podemos modificar el tamaño de la ventana

# EJEMPLO DE ETIQUETAS --------------------------------------------------------------------------------------------------------------------------

# nombre - objeto tkinter - .Label con mayuscula inicial - donde va a
# vivir - que quiero que diga la etiqueta
label = tkinter.Label(windows, text="Hola Mundo usando solo pack", bg = "blue") # con bg le damos color a la eqtiqueta
label_two = tkinter.Label(windows, text="Hola Mundo con BOTTOM")
label_three = tkinter.Label(windows, text="Hola Mundo con RIGHT")

# el metodo pack tiene fill (estirar) side (es para posicionar)
# Ponemos la etiqueta en pantalla, pack es el metodo mas censillo
label.pack() #el metodo pack siempre pone el objeto arriba y centrado
# label.pack(fill = tkinter.BOTH, expand = True)
# label.pack(fill = tkinter.X) #abarcara todo el eje x de la ventana
# label.pack(fill = tkinter.Y, expand = True) #abarcara todo el eje y de la ventana
label_two.pack(side = tkinter.BOTTOM)
label_three.pack(side = tkinter.RIGHT)


# EJEMPLO DE BOTONES --------------------------------------------------------------------------------------------------------------------------

button = tkinter.Button(windows, text = "Presioname")
button.pack()

# Hacemos una funcion para darle utilidad a un boton
def greeting():
    print("Hola")

# Ahora le damos esa funcionalidad a un boton, llamamos la funcion 
# SIN PARENTESIS ya que con ellos la funcion se activa automaticamente
#  y ya cuando se le da click al boton no sucede absolutamente nada
button_two = tkinter.Button(windows, text="Saludar", command = greeting)
button_two.pack()

# Funcion con parametros
def greeting_two(name):
    print("hola " + name)

# Usamos lambda para pasarle parametros a la funcion
button_three = tkinter.Button(windows, text="Saludo Personalizado", command = lambda: greeting_two("python"))
button_three.pack()

# lambda tambien sirve para declarar la funcion en una sola linea de codigo
button_four = tkinter.Button(windows, text="Saludo con lambda", command = lambda: print("Hola con solo lambda"))
button_four.pack()


# EJEMPLO DE CAJAS DE TEXTO --------------------------------------------------------------------------------------------------------------------------

textbox = tkinter.Entry(windows)
textbox.pack()


# Este mainloop llevara el registro de todo lo que sucedera en la ventana
windows.mainloop()