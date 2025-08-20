#!/usr/bin/env python3
#-----Librerie-----#
from datetime import timedelta  #Per recapitare la data
import requests #Per richiedere l'immagine a Internet
from datetime import datetime #Per recuperare la data
import os
import pyautogui
import sys
import PNG
import END
#-----Fine Librerie e Import-----#
 
#-----Recupero immagini da Internet-----#
now = datetime.now()

dataz = now.strftime("%Y%m%d")
ora = int(now.strftime("%H"))

if ora<18:
    dataz=dataz+"00"
else:
    dataz=dataz+"12"

try:

    response1 = requests.get("https://modeles16.meteociel.fr/modeles/gensp/runs/"+dataz+"/graphe3_20000___8.5409_39.3064_.gif", timeout=5)
    file = open("./spaghi_temp_prec.gif", "wb")
    file.write(response1.content)
    file.close()
    response2 = requests.get("https://modeles16.meteociel.fr/modeles/gensp/runs/"+dataz+"/graphe11_20000___8.5409_39.3064_.gif", timeout=5)
    file = open("./spaghi_venti.gif", "wb")
    file.write(response2.content)
    file.close()

except:
    try:
        os.remove("./spaghi_temp_prec.gif")
        os.remove("./spaghi_venti.gif")
    except:
        print("Nessuna immagine da eliminare")
        print("Il sito non è reperibile al momento...")


#-----Fine Recupero-----#

#--------------------Classe main--------------------#
class main():
        today = datetime.now()   #Recapitazione data
        giorni = [1,1,1]    #Creazione oggetto che conterrà l'oggetto data
        data = ["","",""]   #Creazione Array che conterrà la data in stringa
        oggetti = [1,1,1]   #Creazione Array che conterrà oggetti di classe 'PNG_Maker' che faranno eseguire tutto il programma 3 volte
        for i in range(3):
            giorni[i] = today + timedelta(days = i+1)  #Recapitazione data
            data[i] = giorni[i].strftime("%d/%m/%Y")    #Metodo parse per assegnare la data all'Array 'data[]'
            oggetti[i] = PNG.PNG_Maker(data[i], str(i+1)+".png")  #Creazione oggetto di classe 'PNG_Maker'
        close = END.close()   #Creazione oggetto di classe 'close'
#--------------------Fine Classe main--------------------#
