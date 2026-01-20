#!/usr/bin/env python3
#-----Librerie-----#
#Version: 11.2#

from datetime import timedelta  #Per recapitare la data
import requests #Per richiedere l'immagine a Internet
from datetime import datetime #Per recuperare la data
import os
import pyautogui
import sys
import PNG
import END
import INTERFACE # Import necessario per la ProgressWindow
import ftplib    # Per l'upload FTP
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
    def __init__(self):
        today = datetime.now()   #Recapitazione data
        giorni = [1,1,1]    #Creazione oggetto che conterrà l'oggetto data
        data = ["","",""]   #Creazione Array che conterrà la data in stringa
        oggetti = [1,1,1]   #Creazione Array che conterrà oggetti di classe 'PNG_Maker'

        # Fase 1: Generazione Immagini (Richiede interazione utente)
        # Non usiamo la progress bar qui perché bloccherebbe l'interfaccia di input
        for i in range(3):
            giorni[i] = today + timedelta(days = i+1)  #Recapitazione data
            data[i] = giorni[i].strftime("%d/%m/%Y")    #Metodo parse per assegnare la data all'Array 'data[]'
            # Questo apre l'interfaccia grafica per ogni giorno
            oggetti[i] = PNG.PNG_Maker(data[i], str(i+1)+".png")

        # Fase 2: Upload FTP (Automatica)
        # Qui usiamo la Progress Window perché è un processo automatico che richiede tempo

        # 1 step connessione + 3 step upload = 4 step totali
        p_win = INTERFACE.ProgressWindow(4)
        p_win.update_text("Connessione al server FTP in corso...")

        # DATI FTP - DA CONFIGURARE
        ftp_host = "ftp.nomesito.com"
        ftp_user = "USERNAME"   # <-- INSERISCI QUI IL TUO USERNAME
        ftp_pass = "PASSWORD"   # <-- INSERISCI QUI LA TUA PASSWORD
        ftp_path = "/percorso_upload"

        try:
            # Connessione al server FTP
            session = ftplib.FTP(ftp_host, ftp_user, ftp_pass)
            p_win.step() # Step 1 completato

            # Cambio cartella di destinazione
            session.cwd(ftp_path)

            # File da caricare (che si trovano nella cartella 'pronte')
            files_to_upload = ["1.png", "2.png", "3.png"]

            for filename in files_to_upload:
                p_win.update_text(f"Upload di {filename}...")

                # Costruisci il percorso locale (es. ./pronte/1.png)
                local_path = os.path.join("./pronte", filename)

                if os.path.exists(local_path):
                    with open(local_path, "rb") as file:
                        # Comando STOR per caricare il file in binario
                        session.storbinary(f"STOR {filename}", file)
                else:
                    print(f"File locale mancante: {local_path}")

                # Avanza step per ogni file caricato
                p_win.step()

            session.quit()
            p_win.update_text("Upload completato.")

        except Exception as e:
            p_win.update_text(f"Errore FTP!")
            print(f"Errore durante l'upload FTP: {e}")

        # Chiudi la finestra di progresso
        p_win.close()

        # Mostra finestra finale
        close = END.close()
#_--------------------Fine Classe main--------------------_#

if __name__ == "__main__":
    main()
