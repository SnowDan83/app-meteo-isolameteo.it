#!/usr/bin/env python3
#-----Librerie-----#
#Version: 11.2#

import urllib.request as urllib2
from wand.image import Image    #Creazione immagine
from wand.display import display    #Creazione immagine
from wand.drawing import Drawing    #Creazione immagine
from wand.color import Color    #Creazione immagine
from typing import NewType
import os
from os import path
import shutil
import INTERFACE    
#-----Fine Librerie e Import-----#


#-----Inizializzazione variabili globali-----#
#Array 'coordx[]' per coordinate posizionamento immagini condizioni
coordx=[55,155,75,160,65,160,345,445,365,455,345,455,645,745,665,755,665,755]
#Array 'coordy[]' per coordinate posizionamento immagini condizioni
coordy=[75,30,195,160,320,280,75,30,195,160,320,280,75,30,195,160,320,280]
#Array 'coordv[]' per coordinate posizionamento immagini venti
coordv=[90,30,255,170,385,325,550,465,690,620,845,765]
#Array 'coordw[]' per coordinate posizionamento immagini venti
coordw=[30,240,215,390,30,240,215,390,30,240,215,390]
#-----Fine inizializzazione variabili globali-----#


#--------------------Classe PNG_Maker--------------------#
class PNG_Maker():

    def __init__(self, giuorno, nuome): #Costruttore della classe PNG_Maker
        o = INTERFACE.UI()     #Creazione oggetto di classe UI
        self.makeImage(o, giuorno, nuome)   #Metodo tramite il quale si creano le immagini, con il passaggio di giorno da stampare su immagine e nome con il quale salvare il file


    def makeImage(self, o, giuorno, nuome): #Metodo principale classe PNG_Maker
        for i in range(30): #30 iterazioni, una per ogni immagine delle condizioni da applicare
            if i<18:    #Posizione delle condizioni
                if i==0:    #Scelta prima immagine da usare come base
                    z='./base.png'
                else:
                    z='./base_prov.png'
                with Image(filename=z) as bg_img:   #Scelta immagine
                    with Image(filename=o.urlF[i]) as zona_img: #Scelta immagine
                        bg_img.composite(zona_img, left=coordx[i], top=coordy[i])   #Composizione immagine
                        bg_img.save(filename='./base_prov.png')   #Salvataggio immagine
            elif i>=18: #Posizione dei venti
                with Image(filename='./base_prov.png') as bg_img: #Scelta immagine
                    with Image(filename=o.urlF[i]) as zona_img: #Scelta immagine
                        bg_img.composite(zona_img, left=coordv[i-18], top=coordw[i-18]) #Composizione immagine
                        bg_img.save(filename='./base_prov.png')   #Salvataggio immagine

        #-----Applicazione Immagine Temperatura-----#
        with Image(filename='./base_prov.png') as bg_img: #Scelta immagine
            with Image(filename=o.urlF[30]) as temp_img:    #Scelta immagine
                bg_img.composite(temp_img, left=545, top=370)   #Composizione immagine
                bg_img.save(filename='quasi.png')   #Salvataggio immagine

        #-----Applicazione Scritta Data-----
        stringaGiorno = str(giuorno)    #Metodo parse per convertire il giorno
        stringaNome = str(nuome)    #Metodo parse per convertire il nome del file

        with Drawing() as draw:
          with Image(filename = "./quasi.png") as img:    #Scelta immagine
            draw.font = '/usr/share/fonts/noto/NotoSans-Regular.ttf' #Font scritta
            draw.font_size = 16 #Dimensione scritta
            draw.fill_color=Color('yellow') #Colore scritta
            draw.text(510, 22, stringaGiorno)   #Scrittura data
            draw(img)
            img.save(filename = stringaNome)    #Salvataggio immagine
        img.close() #Chiusura immagine


        #Spostamento file
        src = "./"
        dst = "./pronte"
        files = [i for i in os.listdir(src) if i.startswith(stringaNome) and path.isfile(path.join(src, i))]
        for f in files:
            shutil.move(os.path.join(src, f), os.path.join(dst, f))
#--------------------Fine Classe PNG_Maker--------------------#
