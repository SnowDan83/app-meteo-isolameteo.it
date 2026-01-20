## 🌦️ App Meteo - Isolameteo.it

Applicazione desktop avanzata per la generazione automatizzata di grafiche meteorologiche per la Sardegna. Il software permette di scaricare dati modellistici, personalizzare le previsioni per diverse località tramite interfaccia grafica, generare immagini PNG composte e caricarle automaticamente su un server FTP.

Versione: 11.2
## 📜 Funzionamento del Software

Il flusso di lavoro dell'applicazione è gestito da diversi moduli integrati:

    Avvio e Download Dati (START.pyw):

        Calcola la data e l'ora attuali per determinare il run modellistico corretto.

        Scarica automaticamente i grafici "spaghi" (temperatura e vento) da meteociel.fr per l'area della Sardegna.

    Interfaccia Utente (INTERFACE.py):

        Mostra i grafici scaricati come riferimento.

        Presenta un'interfaccia responsive (si adatta alla risoluzione dello schermo usando PyAutoGUI).

        Permette di impostare le condizioni per 6 località chiave: Sassari, Olbia, Oristano, Nuoro, Iglesias, Cagliari.

        Permette di definire i venti (Nord, Ovest, Est, Sud) e il trend termico.

    Generazione Grafica (PNG.py):

        Utilizza la libreria Wand (ImageMagick) per comporre le icone meteo, le frecce del vento e le temperature sulla mappa base della Sardegna.

        Salva le immagini generate nella cartella ./pronte.

    Upload Automatico (START.pyw e INTERFACE.py):

        Al termine della generazione dei 3 giorni, avvia una finestra di progresso.

        Si connette a un server FTP pre-configurato e carica le immagini (1.png, 2.png, 3.png).

## 🛠️ Requisiti e Installazione
Prerequisiti di Sistema

Poiché l'app utilizza la libreria Wand, è necessario avere installato ImageMagick sul sistema operativo.

    Windows: Scaricare e installare ImageMagick. Durante l'installazione, assicurarsi di spuntare la casella "Install development headers and libraries for C and C++".

Dipendenze Python

Il progetto utilizza un file requirements.txt per la gestione delle librerie. Le principali sono:

    Wand: Per l'elaborazione delle immagini.

    PyAutoGUI: Per il ridimensionamento della GUI in base allo schermo.

    requests: Per il download dei grafici meteo.

    tkinter: Per l'interfaccia grafica (inclusa standard in Python).

Per installare tutte le dipendenze necessarie, eseguire:
Bash

pip install -r requirements.txt

Nota: Il file requirements.txt include versioni specifiche (es. Wand==0.6.13, requests==2.32.5) per garantire la compatibilità.
⚙️ Configurazione FTP

Prima di utilizzare la funzione di upload automatico, è necessario configurare le credenziali FTP nel file START.pyw.

Aprire START.pyw con un editor di testo e cercare la sezione:
Python

## DATI FTP - DA CONFIGURARE
ftp_host = "ftp.nomesito.com"
ftp_user = "USERNAME"   # <-- INSERISCI QUI IL TUO USERNAME
ftp_pass = "PASSWORD"   # <-- INSERISCI QUI LA TUA PASSWORD
ftp_path = "/percorso_upload"

Sostituire i valori con quelli del proprio server.
🚀 Utilizzo

    Assicurarsi che la struttura delle cartelle sia corretta (cartella icone presente, cartella pronte presente).

    Eseguire lo script principale:

Bash

python START.pyw

    L'applicazione richiederà di inserire le previsioni per il Giorno 1, poi il Giorno 2 e infine il Giorno 3.

    Al termine dell'inserimento, l'app mostrerà una barra di caricamento per l'upload FTP e confermerà il successo dell'operazione.

## 📂 Struttura dei File

    START.pyw: Script principale (Download, Loop giorni, Upload FTP).

    INTERFACE.py: Gestione GUI, Layout Griglia, Finestra di Progresso.

    PNG.py: Motore grafico per la creazione dei file .png.

    END.py: Finestra di conferma chiusura.

    base.png: Mappa base della Sardegna.

    /icone: Cartella contenente tutte le risorse grafiche (meteo, venti, temperature).

    /pronte: Cartella di destinazione per le immagini generate.

## ✍️ Autori

    Daniele Concas

    Daniele Sanna

© 2026 - Isolameteo.it
