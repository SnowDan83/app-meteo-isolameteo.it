# 🌦️ App Meteo - Isolameteo.it

**App Meteo** è un software desktop sviluppato per l'automazione delle previsioni grafiche di Isolameteo.it. L'applicazione gestisce l'intero flusso di lavoro: dal download dei dati modellistici alla generazione di mappe meteorologiche personalizzate per la Sardegna, fino alla pubblicazione automatica su server FTP.

**Versione:** 11.2

---

## 📋 Panoramica del Funzionamento

L'architettura del software è modulare e suddivisa in quattro fasi logiche distinte:

1.  **Acquisizione Dati (`START.pyw`)**
    * Identificazione automatica del run modellistico più recente in base all'orario di esecuzione.
    * Download dei grafici previsionali ("spaghi" per temperatura e vento) dalla fonte *meteociel.fr*.
2.  **Configurazione Previsione (`INTERFACE.py`)**
    * Visualizzazione dei dati scaricati tramite interfaccia grafica (GUI) adattiva.
    * Input manuale delle condizioni meteorologiche per le località target: Sassari, Olbia, Oristano, Nuoro, Iglesias e Cagliari.
    * Definizione dei parametri di vento (direzione e intensità) e tendenza termica.
3.  **Elaborazione Grafica (`PNG.py`)**
    * Composizione delle immagini finali utilizzando la libreria `Wand` (ImageMagick).
    * Sovrapposizione dinamica di icone meteo, frecce del vento e indicatori di temperatura sulla mappa base della Sardegna.
4.  **Pubblicazione (`START.pyw`)**
    * Connessione automatica al server FTP.
    * Upload dei file generati (`1.png`, `2.png`, `3.png`) nella directory remota specificata.

---

## ⚙️ Requisiti di Sistema

### Prerequisiti Software
Il corretto funzionamento del motore grafico richiede l'installazione di **ImageMagick**:
* **Windows**: Scaricare l'eseguibile dal [sito ufficiale](https://imagemagick.org/script/download.php#windows).
    * ⚠️ **Importante**: Durante l'installazione, selezionare l'opzione *"Install development headers and libraries for C and C++"*.

### Dipendenze Python
Il progetto necessita delle librerie elencate nel file `requirements.txt`. Le dipendenze principali includono:
* `Wand`: Gestione ed elaborazione delle immagini.
* `PyAutoGUI`: Adattamento della risoluzione dell'interfaccia.
* `requests`: Gestione delle richieste HTTP per il download dei dati.
* `tkinter`: Libreria standard per l'interfaccia grafica.

Per installare l'ambiente, eseguire il comando:
```bash
pip install -r requirements.txt

```

---

## 🔧 Configurazione

Prima del primo utilizzo, è necessario configurare i parametri di accesso al server FTP.

1. Aprire il file `START.pyw` con un editor di testo.
2. Individuare la sezione di configurazione (riga ~70):
3. Inserire le proprie credenziali sostituendo i valori placeholder:

```python
# DATI FTP - DA CONFIGURARE
ftp_host = "ftp.tuosito.com"
ftp_user = "TUO_USERNAME"
ftp_pass = "TUA_PASSWORD"
ftp_path = "/percorso_remoto_upload"

```

---

## 🚀 Guida all'Uso

1. **Verifica Preliminare**: Assicurarsi che nella directory del programma siano presenti le cartelle `./icone` e `./pronte`.
2. **Avvio**: Eseguire lo script principale:
```bash
python START.pyw

```


3. **Input Dati**:
* L'interfaccia richiederà l'inserimento delle condizioni per 3 giorni consecutivi (Giorno 1, Giorno 2, Giorno 3).
* Selezionare le opzioni dai menu a tendina per ogni località e parametro.


4. **Generazione e Upload**:
* Al termine dell'inserimento, il sistema genererà le immagini.
* Una finestra di dialogo mostrerà l'avanzamento dell'upload FTP.
* La procedura terminerà con un messaggio di conferma.



---

## 📂 Struttura del Progetto

* `START.pyw`: Script di avvio, gestisce il download dei dati e il client FTP.
* `INTERFACE.py`: Gestisce il layout grafico e la finestra di progresso.
* `PNG.py`: Modulo core per l'elaborazione e la creazione delle immagini PNG.
* `END.py`: Modulo per la notifica di completamento operazioni.
* `requirements.txt`: Elenco delle dipendenze necessarie.

---

## ✍️ Autori

* **Daniele Concas**
* **Daniele Sanna**

© 2026 - Isolameteo.it

```

```
