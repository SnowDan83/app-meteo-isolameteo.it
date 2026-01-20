#!/usr/bin/env python3
#-----Librerie-----#
#Version: 11.2#

from tkinter import *   #Interfaccia Grafica
import tkinter as tk    #Interfaccia Grafica
import math
import os
#-----Fine Librerie-----#

#--------------------Classe close--------------------#
class close():
    def __init__(self): #Costruttore della classe close
        self.lastWindow()   #Metodo tramite il quale si esegue il metodo lastWindow

    def lastWindow(self):   #Metodo che fa comparire l'ultima finestra di informazioni
            # Create the main window
            window = tk.Tk()
            window.title("isolameteo.it")
            window.geometry("500x300")
            imgicon = PhotoImage(file=os.path.join("./icone/","icon.png"))    #Configurazione finestra
            window.tk.call('wm', 'iconphoto', window._w, imgicon)   #Configurazione finestra
            window.config(background="#2f343f")   #Configurazione finestra

            # Create a label widget
            label = tk.Label(
                window,
                text="Immagini Generate\nCorrettamente :-)\n\n",
                anchor="center",
                width=25,
                bg="#2f343f",
                fg="white",
                font =("Notosans", 14)
            )
            widget = Button(text='EXIT')
            widget.config(bd=4, relief=RAISED)
            widget.config(bg="#2f343f", fg="white")
            widget.config(font=('Notosans', 10, 'bold'))
            widget.config(command=window.destroy)

            # Pack the label widget to display it
            label.pack()
            widget.pack()

            # Run the application
            window.mainloop()

