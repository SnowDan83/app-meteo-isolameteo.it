#!/usr/bin/env python3
#-----Librerie-----#
import urllib.request as urllib2
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
import os
from os import path
import shutil
import INTERFACE    
#-----Fine Librerie e Import-----#

class PNG_Maker():
    def __init__(self, giuorno, nuome): 
        o = INTERFACE.UI()     
        self.makeImage(o, giuorno, nuome)   

    def makeImage(self, o, giuorno, nuome): 
        # [Logica icone e temperature invariata]
        coordx=[55,155,75,160,65,160,345,445,365,455,345,455,645,745,665,755,665,755]
        coordy=[75,30,195,160,320,280,75,30,195,160,320,280,75,30,195,160,320,280]
        coordv=[90,30,255,170,385,325,550,465,690,620,845,765]
        coordw=[30,240,215,390,30,240,215,390,30,240,215,390]

        for i in range(30): 
            z = './base.png' if i == 0 else './base_prov.png'
            tx = coordx[i] if i < 18 else coordv[i-18]
            ty = coordy[i] if i < 18 else coordw[i-18]
            with Image(filename=z) as bg_img:   
                with Image(filename=o.urlF[i]) as zona_img: 
                    bg_img.composite(zona_img, left=tx, top=ty)   
                    bg_img.save(filename='./base_prov.png')   

        with Image(filename='./base_prov.png') as bg_img: 
            with Image(filename=o.urlF[30]) as temp_img:    
                bg_img.composite(temp_img, left=545, top=370)   
                bg_img.save(filename='quasi.png')   

        #----- LOGICA DATA CROSS-DISTRO (Arch e Ubuntu) -----#
        stringaGiorno = str(giuorno)
        stringaNome = str(nuome)

        with Drawing() as draw:
            # Lista di percorsi reali per font "Sans" comuni su Arch e Ubuntu
            font_paths = [
                "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",          # Arch Linux (Standard)
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", # Ubuntu (Standard)
                "/usr/share/fonts/TTF/LiberationSans-Bold.ttf",      # Arch Alternative
                "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", # Ubuntu Alternative
                "/usr/share/fonts/TTF/Arial.ttf"                     # Se hai i font MS su Arch
            ]
            
            # Seleziona il primo font che esiste davvero sul disco
            for p in font_paths:
                if os.path.exists(p):
                    draw.font = p
                    break
            
            draw.font_size = 18
            draw.fill_color = Color('yellow')
            
            # Aggiungiamo un'ombra nera (stroke) per garantire la leggibilità su Arch
            draw.stroke_color = Color('black')
            draw.stroke_width = 1
            
            with Image(filename="./quasi.png") as img:
                # Disegna il testo
                draw.text(480, 15, stringaGiorno) 
                draw(img)
                # Salva l'immagine finale
                img.save(filename=stringaNome)

        # Spostamento file nella cartella 'pronte'
        dst = "./pronte"
        if not os.path.exists(dst): os.makedirs(dst)
        if os.path.exists(stringaNome):
            shutil.move(stringaNome, os.path.join(dst, stringaNome))
