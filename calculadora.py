from tkinter import *
from math import *
ventana = Tk()
ventana.title("Conversor a Romanos")
ventana.geometry("300x400")
ventana.resizable(False, False)
ventana.configure(bg="gray42")

color_boton = "gray99"
ancho_boton = 8
alto_boton = 2
operador = ""
texto_pantalla = StringVar()


def clear():
    global operador
    operador = ""
    texto_pantalla.set("0")


def click_boton(boton):
    global operador
    operador += str(boton)
    texto_pantalla.set(operador)


def resultado():
    texto_pantalla.set(roman(operador))


roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def roman(operador):

    x = int(operador)

    y = 0
    Str = ""
    for i, r in roman_map:
        
        y = x//i

        for j in range(0, y):
            
            Str = Str+r

        
        x = x % i

    return Str


# Botones
Boton1 = Button(ventana, text="1", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(1)).grid(row=1, column=0, padx=5, pady=15)
Boton2 = Button(ventana, text="2", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(2)).grid(row=1, column=1, padx=5, pady=15)
Boton3 = Button(ventana, text="3", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(3)).grid(row=1, column=2, padx=5, pady=15)
Boton4 = Button(ventana, text="4", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(4)).grid(row=2, column=0, padx=0, pady=15)
Boton5 = Button(ventana, text="5", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(5)).grid(row=2, column=1, padx=5, pady=15)
Boton6 = Button(ventana, text="6", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(6)).grid(row=2, column=2, padx=5, pady=15)
Boton7 = Button(ventana, text="7", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(7)).grid(row=3, column=0, padx=0, pady=15)
Boton8 = Button(ventana, text="8", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(8)).grid(row=3, column=1, padx=5, pady=15)
Boton9 = Button(ventana, text="9", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(9)).grid(row=3, column=2, padx=5, pady=15)
Botonc = Button(ventana, text="C", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=clear).grid(row=4, column=0, padx=0, pady=15)
Boton0 = Button(ventana, text="0", bg=color_boton,
                width=ancho_boton, height=alto_boton, command=lambda: click_boton(0)).grid(row=4, column=1, padx=5, pady=15)
Botonigual = Button(ventana, text="=", bg=color_boton,
                    width=ancho_boton, height=alto_boton, command=resultado).grid(row=4, column=2, padx=5, pady=15)


Pantalla = Entry(ventana, font=("arial", 15, "bold"),
                 width=22, borderwidth=10, bg="CadetBlue1", textvariable=texto_pantalla)
Pantalla.grid(row=0, column=0, columnspan=3, padx=15, pady=10)


ventana.mainloop()
