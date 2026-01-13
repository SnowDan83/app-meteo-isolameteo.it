#!/usr/bin/env python3
#-----Librerie-----#
from tkinter import * #Interfaccia Grafica
from tkinter import ttk #Per la Progressbar
import tkinter as tk    #Interfaccia Grafica
from typing import NewType
import os
import pyautogui
#-----Fine Librerie e Import-----#

#-----Inizializzazione variabili globali-----#
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
        # FIX: Controllo se esiste già una root window attiva
        if tk._default_root is None:
            root = Tk()
        else:
            root = Toplevel()

        root.title('App Meteo')

        # Gestione Icona
        try:
            imgicon = PhotoImage(master=root, file=os.path.join("./icone/", "icon.png"))
            # 'wm iconphoto' funziona solo su finestre top-level o root
            try:
                root.tk.call('wm', 'iconphoto', root._w, imgicon)
            except:
                pass
        except TclError:
            pass

        #---------- Logica di Scaling ----------#
        screen_w, screen_h = pyautogui.size()
        base_width = 1920
        base_height = 1080
        scale_factor = min(screen_w / base_width, screen_h / base_height)

        app_width = int(1920 * scale_factor)
        app_height = int(1080 * scale_factor)

        # Font principale
        font_size = max(int(13 * scale_factor), 8)
        menu_font_size = max(int(8 * scale_factor), 7)

        xw=(screen_w/2)-(app_width/2)
        yh=(screen_h/2)-(app_height/2)
        root.geometry(f'{app_width}x{app_height}+{int(xw)}+{int(yh)}')
        root.config(background="#2f343f")

        #---------- Configurazione Griglia ----------#
        for i in range(10):
            root.columnconfigure(i, weight=1, uniform="cols")

        for i in range(15):
             root.rowconfigure(i, weight=1)

        # Immagini "spaghi"
        # IMPORTANTE: Usare master=root per legare l'immagine a questa specifica finestra
        try:
            img2=PhotoImage(master=root, file='./spaghi_temp_prec.gif')
            img3=PhotoImage(master=root, file='./spaghi_venti.gif')
        except:
            img2 = PhotoImage(master=root, file='./offline.png')
            img3 = PhotoImage(master=root, file='./offline.png')

        label_img2 = Label(root, image=img2, background="#2f343f")
        label_img3 = Label(root, image=img3, background="#2f343f")

        # Manteniamo un riferimento alle immagini per evitare che il garbage collector le cancelli
        label_img2.image = img2
        label_img3.image = img3

        label_img2.grid(row=5, column=0, columnspan=4, rowspan=30, sticky="nsew")
        label_img3.grid(row=5, column=6, columnspan=4, rowspan=30, sticky="nsew")

        # Inizializzazione StringVar
        for i in range(3):
            for j in range(10):
                url[i][j] = StringVar(root)
        temperature = StringVar(root)

        vertical_padding = int(5 * scale_factor)

        # Creazione Etichette e Menu a tendina
        for i in range(4):
            for j in range(10):
                if i==0:
                    Label(root, bg="#2f343f", fg="white", font=("NotoSans", font_size, "bold"),
                          text=luoghi[j], justify="center").grid(row=1, column=j, sticky="nsew", pady=(10, 5))
                else:
                    if j<=5 and i!=3:
                        popupMenu = OptionMenu(root, url[i-1][j], *condizioni)
                    elif j<=5 and i==3:
                        popupMenu = OptionMenu(root, url[i-1][j], *condnotte)
                    else:
                        popupMenu = OptionMenu(root, url[i-1][j], *wind)

                    popupMenu.config(bg="#404552", fg="#d3dae3", bd=0, highlightthickness=0)
                    popupMenu.config(font=("NotoSans", menu_font_size))

                    menu = popupMenu["menu"]
                    menu.config(bg="#404552", fg="#d3dae3", font=("NotoSans", menu_font_size), bd=0)

                    popupMenu.grid(row=i+1, column=j, sticky="ew", padx=5, pady=2, ipady=vertical_padding)

        # Elementi Centrali
        Label(root, bg="#2f343f", fg="#d3dae3", font=("NotoSans", font_size), text="Temperatura").grid(row=5, column=4, columnspan=2, sticky="s")

        tempMenu = OptionMenu(root, temperature, *temp)
        tempMenu.config(bg="#404552", fg="#d3dae3", bd=0, highlightthickness=0, font=("NotoSans", menu_font_size))
        tempMenu["menu"].config(bg="#404552", fg="#d3dae3", font=("NotoSans", menu_font_size), bd=0)
        tempMenu.grid(row=6, column=4, columnspan=2, sticky="ew", padx=10, pady=2, ipady=vertical_padding)

        # Il comando destroy qui chiuder solo questa finestra, permettendo al codice di proseguire
        Button(root, font=("NotoSans", font_size, "bold"), text="Genera Immagine", command=root.destroy).grid(row=7, column=4, columnspan=2, sticky="ew", padx=10, pady=10, ipady=vertical_padding)

        # Informazioni in basso
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Created by:").grid(row=8, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Daniele Concas").grid(row=9, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="red",font=("NotoSans",font_size), text="Daniele Sanna").grid(row=10, column=4, columnspan=2, sticky="n")
        Label(root,bg="#2f343f",fg="green",font=("NotoSans",font_size), text="Version: 10.7").grid(row=11, column=4, columnspan=2, sticky="s")
        Label(root,bg="#2f343f",fg="green",font=("NotoSans",font_size), text="Data: 21/12/2025").grid(row=12, column=4, columnspan=2, sticky="n")
        Label(root,bg="#2f343f",fg="white",font=("NotoSans",font_size), text="© 2025 - Isolameteo.it").grid(row=13, column=4, columnspan=2, sticky="n")

        # Se root è Tk (principale), mainloop blocca qui. Se è Toplevel, wait_window blocca qui.
        if isinstance(root, Tk):
            root.mainloop()
        else:
            root.wait_window()

        #----- Logica di assegnazione dati -----#
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

#--------------------Classe Finestra di Progresso--------------------#
class ProgressWindow():
    def __init__(self, totale_step):
        # Usiamo Toplevel invece di Tk se esiste già una root (anche nascosta)
        if tk._default_root is None:
            self.root = Tk()
        else:
            self.root = Toplevel()

        self.root.title("Elaborazione...")
        self.root.config(background="#2f343f")

        # Centra la finestra
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        w = 400
        h = 180
        x = (screen_w/2) - (w/2)
        y = (screen_h/2) - (h/2)
        self.root.geometry(f'{w}x{h}+{int(x)}+{int(y)}')

        try:
            imgicon = PhotoImage(master=self.root, file=os.path.join("./icone/", "icon.png"))
            try:
                self.root.tk.call('wm', 'iconphoto', self.root._w, imgicon)
            except: pass
        except:
            pass

        # Titolo
        self.lbl_title = Label(self.root, text="Elaborazione in corso...",
                               bg="#2f343f", fg="white", font=("NotoSans", 14, "bold"))
        self.lbl_title.pack(pady=(20, 10))

        # Testo descrittivo azione corrente
        self.lbl_status = Label(self.root, text="Avvio...",
                                bg="#2f343f", fg="#d3dae3", font=("NotoSans", 10))
        self.lbl_status.pack(pady=5)

        # Barra di progresso
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Horizontal.TProgressbar", background="#5294e2", troughcolor="#404552", bordercolor="#2f343f")

        self.progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=300, mode='determinate', style="Horizontal.TProgressbar")
        self.progress.pack(pady=15)

        self.progress["maximum"] = totale_step
        self.step_val = 0

        self.root.update()

    def update_text(self, text):
        """Aggiorna solo il testo dello stato"""
        self.lbl_status.config(text=text)
        self.root.update()

    def step(self, text=None):
        """Avanza la barra e opzionalmente cambia testo"""
        self.step_val += 1
        self.progress["value"] = self.step_val
        if text:
            self.lbl_status.config(text=text)
        self.root.update()

    def close(self):
        self.root.destroy()
