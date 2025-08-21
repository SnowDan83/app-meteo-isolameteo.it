# App Meteo - Isolameteo.it

Questa è una semplice applicazione desktop per generare immagini di previsioni meteo per la Sardegna. L'applicazione utilizza un'interfaccia grafica per consentire all'utente di selezionare le condizioni meteorologiche, il vento e le temperature per diverse località dell'isola per i successivi tre giorni.

## 📜 Descrizione

Il progetto è composto da diversi moduli Python che lavorano insieme:

  * **START.pyw**: Lo script principale che avvia l'applicazione. Scarica i grafici meteorologici (spaghi) da fonti esterne e avvia il processo di generazione delle immagini.
  * **INTERFACE.py**: Crea l'interfaccia utente grafica (GUI) utilizzando `tkinter`. Attraverso questa interfaccia, l'utente può inserire le previsioni per i giorni successivi.
  * **PNG.py**: Si occupa della creazione delle immagini di previsione. Utilizza la libreria `Wand` per comporre le icone meteorologiche su una mappa base della Sardegna in base alle selezioni dell'utente.
  * **END.py**: Mostra una finestra di conferma al termine della generazione delle immagini.

## ✨ Funzionalità Principali

  * **Interfaccia Grafica Semplice**: Un'interfaccia intuitiva basata su `tkinter` per un facile inserimento dei dati.
  * **Dati Esterni**: Recupera i grafici di temperatura e vento dal sito `meteociel.fr`.
  * **Generazione di Immagini**: Crea immagini di previsione personalizzate per 3 giorni (mattina, pomeriggio/sera, notte).
  * **Personalizzazione**: L'utente può selezionare le condizioni del tempo (sereno, nuvoloso, pioggia, neve, etc.), la direzione e l'intensità del vento, e l'andamento della temperatura (in aumento, stazionaria, in calo).

## 🚀 Come Eseguire il Progetto

Per avviare l'applicazione, esegui lo script `START.pyw`:

```bash
python START.pyw
```

Assicurati di avere tutte le dipendenze necessarie installate.

## 📦 Dipendenze

Il progetto richiede le seguenti librerie Python:

  * `requests`
  * `pyautogui`
  * `Wand` (potrebbe richiedere l'installazione di ImageMagick)
  * `tkinter` (generalmente inclusa con Python)

Puoi installarle usando pip:

```bash
pip install requests pyautogui Wand
```

## ✍️ Autori

  * Daniele Concas
  * Daniele Sanna
