#!/usr/bin/env python3
#-----Librerie-----#
from tkinter import * #Interfaccia Grafica
import tkinter as tk    #Interfaccia Grafica
from typing import NewType
import os
import pyautogui
#-----Fine Librerie e Import-----#

#-----Inizializzazione variabili globali-----#
# MODIFICA 1: Ho messo "\n" nei venti per mandare il testo a capo e risparmiare larghezza
luoghi = ["Sassari:", "Olbia:", "Oristano:", "Nuoro:", "Iglesias:", "Cagliari:", "Vento\nNord:", "Vento\nOvest:", "Vento\nEst:", "Vento\nSud:"]
condnotte = ["Sereno notte","Poco Nuv. notte","Nuv. Sparse notte","Var. Pioggia notte","Var. Temporale notte","Var. misto Neve notte","Var. Neve notte","Coperto","Pioggia","Temporale","Misto Neve","Neve"]
condizioni = ["Sereno","Poco Nuv.","Nuv. Sparse","Var. Pioggia","Var. Temporale","Var. misto Neve","Var. Neve","Coperto","Pioggia","Temporale","Misto Neve","Neve"]
wind = ["N-deb","N-for","NE-deb","NE-for","E-deb","E-for","SE-deb","SE-for","S-deb","S-for","SW-deb","SW-for","W-deb","W-for","NW-deb","NW-for"]
temp = ["Aumento", "Stazionaria", "Calo"]
url = [
    [":",":",":",":",":",":",":",":","",""],
    [":",":",":",":",":",":",":",":","",""],
    [":",":",":",":",":",":",":",":","",""]
]
#-----Fine inizializzazione variabili globali-----#


#--------------------Classe UI--------------------#
class UI():
    urlF = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

    def __init__(self):
        self.getAll()

    def getAll(self):
        root = Tk()
        root.title('App Meteo')
        try:
            imgicon = PhotoImage(file=os.path.join("./icone/", "icon.png"))
            root.tk.call('wm', 'iconphoto', root._w, imgicon)
        except TclError: # CORRETTO: Aggiunto spazio
            pass # Gestione errore se l'icona non esiste

        #---------- Logica di Scaling ----------#
        screen_w, screen_h = pyautogui.size()
        base_width = 1920
        base_height = 1080
        scale_factor = min(screen_w / base_width, screen_h / base_height)
        
        app_width = int(1845 * scale_factor)
        app_height = int(940 * scale_factor)
        
        # Font principale
        font_size = max(int(12 * scale_factor), 8)
        # MODIFICA 3: Font ridotto per i menu (circa 85% del normale)
        menu_font_size = max(int(6 * scale_factor), 7)

        xw=(screen_w/2)-(app_width/2)
        yh=(screen_h/2)-(app_height/2)
        root.geometry(f'{app_width}x{app_height}+{int(xw)}+{int(yh)}')
        root.config(background="#2f343f")
        
        #---------- Configurazione Griglia per Adattabilità ----------#
        # MODIFICA 2: uniform="cols" applicato a TUTTE le colonne (0-9)
        # Questo costringe ogni colonna ad avere la stessa larghezza identica.
        for i in range(10):
            root.columnconfigure(i, weight=1, uniform="cols")
        
        # Righe
        for i in range(15):
             root.rowconfigure(i, weight=1)

        # Immagini "spaghi"
        try:
            img2=PhotoImage(file='./spaghi_temp_prec.gif')
            img3=PhotoImage(file='./spaghi_venti.gif')
        except:
            img2 = PhotoImage(file='./offline.png')
            img3 = PhotoImage(file='./offline.png')

        label_img2 = Label(root, image=img2, background="#2f343f")
        label_img3 = Label(root, image=img3, background="#2f343f")
        
        # Le immagini occupano 4 colonne ciascuna (0-3 e 6-9)
        label_img2.grid(row=5, column=0, columnspan=4, rowspan=30, sticky="nsew")
        label_img3.grid(row=5, column=6, columnspan=4, rowspan=30, sticky="nsew")
        
        # Inizializzazione StringVar
        for i in range(3):
            for j in range(10):
                url[i][j] = StringVar(root)
        temperature = StringVar(root)

        # Padding ridotto per rendere i menu più compatti verticalmente
        vertical_padding = int(5 * scale_factor) 
        
        # Creazione Etichette e Menu a tendina
        for i in range(4):
            for j in range(10):
                if i==0:
                    # Intestazioni (Città e Venti)
                    Label(root, bg="#2f343f", fg="white", font=("NotoSans", font_size, "bold"), 
                          text=luoghi[j], justify="center").grid(row=1, column=j, sticky="nsew", pady=(10, 5))
                else:
                    # Creazione Menu
                    if j<=5 and i!=3:
                        popupMenu = OptionMenu(root, url[i-1][j], *condizioni)
                    elif j<=5 and i==3:
                        popupMenu = OptionMenu(root, url[i-1][j], *condnotte)
                    else:
                        popupMenu = OptionMenu(root, url[i-1][j], *wind)
                    
                    # Stile del Menu
                    popupMenu.config(bg="#404552", fg="#d3dae3", bd=0, highlightthickness=0)
                    # Applico il font ridotto
                    popupMenu.config(font=("NotoSans", menu_font_size))
                    
                    # Menu interno (dropdown)
                    menu = popupMenu["menu"]
                    menu.config(bg="#404552", fg="#d3dae3", font=("NotoSans", menu_font_size), bd=0)
                    
                    # MODIFICA 4: padx=5 per creare spazio tra i pulsanti e farli sembrare centrati nella cella
                    popupMenu.grid(row=i+1, column=j, sticky="ew", padx=5, pady=2, ipady=vertical_padding)

        # Elementi Centrali (Temperatura e Genera)
        Label(root, bg="#2f343f", fg="#d3dae3", font=("NotoSans", font_size), text="Temperatura").grid(row=5, column=4, columnspan=2, sticky="s")
        
        tempMenu = OptionMenu(root, temperature, *temp)
        tempMenu.config(bg="#404552", fg="#d3dae3", bd=0, highlightthickness=0, font=("NotoSans", menu_font_size))
        tempMenu["menu"].config(bg="#404552", fg="#d3dae3", font=("NotoSans", menu_font_size), bd=0)
        tempMenu.grid(row=6, column=4, columnspan=2, sticky="ew", padx=10, pady=2, ipady=vertical_padding)

        Button(root, font=("NotoSans", font_size, "bold"), text="Genera Immagine", command=root.destroy).grid(row=7, column=4, columnspan=2, sticky="ew", padx=10, pady=10, ipady=vertical_padding)

        # Informazioni in basso
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Created by:").grid(row=8, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Daniele Concas").grid(row=9, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Daniele Sanna").grid(row=10, column=4, columnspan=2, sticky="n")
        Label(root,bg="#2f343f",fg="green",font=("NotoSans",font_size), text="Version: 10.4").grid(row=11, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="green",font=("NotoSans",font_size), text="Data: 13/12/2025").grid(row=12, column=4, columnspan=2, sticky="n")
        Label(root,bg="#2f343f",fg="white",font=("NotoSans",font_size), text="© 2025 - Isolameteo.it").grid(row=13, column=4, columnspan=2, sticky="n")

        root.mainloop()

        #----- Logica di assegnazione dati (invariata) -----#
        for i in range(3):
            for j in range(10):
                url[i][j] = url[i][j].get()
                url[i][j] = str(url[i][j])

        contatore=0
        for i in range(3):
            for j in range(6):
                self.urlF[contatore]=url[i][j]
                contatore+=1

        for i in range(3):
            j=6
            while j<10:
                self.urlF[contatore]=url[i][j]
                contatore+=1
                j+=1
        
        for i in range(30):
            self.urlF[i]="./icone/"+self.urlF[i]+"!.png"

        temperature=temperature.get()
        self.urlF[30]="./icone/"+str(temperature)+"!.png"
