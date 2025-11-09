#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox, ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading

# --- WIDGET GALLERIA (SENZA CONTROLLI PROPRI) ---
class ImageGalleryWidget:
    def __init__(self, parent, urls, gallery_title="Galleria"):
        self.parent = parent
        self.urls = urls
        self.images = [None] * len(urls)
        self.current_image_index = 0

        self.main_frame = tk.Frame(parent, bg="#3C3C3C", bd=2, relief="sunken")
        self.main_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # --- Sezione di caricamento ---
        self.loading_frame = tk.Frame(self.main_frame, bg="#3C3C3C")
        self.loading_frame.pack(pady=20, expand=True)

        title_label = tk.Label(self.loading_frame, text=gallery_title, font=("Helvetica", 16, "bold"), bg="#3C3C3C", fg="white")
        title_label.pack(pady=5)

        self.loading_label = tk.Label(self.loading_frame, text="Caricamento...", font=("Helvetica", 12), bg="#3C3C3C", fg="white")
        self.loading_label.pack()
        self.progress_bar = ttk.Progressbar(self.loading_frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        # --- Sezione della galleria (inizialmente nascosta) ---
        self.gallery_frame = tk.Frame(self.main_frame, bg="#2E2E2E")
        self.image_label = tk.Label(self.gallery_frame, bg="#2E2E2E")
        self.image_label.pack(padx=10, pady=10, expand=True)

        # Avvia il caricamento
        self.loading_thread = threading.Thread(target=self.load_images)
        self.loading_thread.start()

    def load_images(self):
        total_images = len(self.urls)
        for i, url in enumerate(self.urls):
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                self.images[i] = ImageTk.PhotoImage(img)

                if self.progress_bar.winfo_exists():
                    self.progress_bar['value'] = (i + 1) / total_images * 100
            except Exception as e:
                print(f"Errore caricamento immagine {url}: {e}")

        self.parent.after(0, self.show_main_interface)

    def show_main_interface(self):
        if not any(self.images):
            self.loading_label.config(text="Caricamento fallito.")
            return

        self.loading_frame.pack_forget()
        self.gallery_frame.pack(expand=True, fill="both")
        self.show_image()

    def show_image(self):
        if self.images[self.current_image_index]:
            self.image_label.config(image=self.images[self.current_image_index])

    # --- METODI PUBBLICI PER IL CONTROLLO ESTERNO ---
    def go_to_previous(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()

    def go_to_next(self):
        if self.current_image_index < len(self.images) - 1:
            self.current_image_index += 1
            self.show_image()


# --- SCRIPT PRINCIPALE DI AVVIO ---
if __name__ == "__main__":
    # 1. Crea la finestra principale
    root = tk.Tk()
    root.title("Dashboard Meteo Sincronizzata")
    root.geometry("1600x900")
    root.configure(bg="#2E2E2E")

    # Frame contenitore per le gallerie
    galleries_container = tk.Frame(root, bg="#2E2E2E")
    galleries_container.pack(fill="both", expand=True)

    # 2. Definisci gli URL per le due gallerie
    gallery1_urls = [f"https://modeles3.meteociel.fr/modeles/icon2i/run/icon2i_it1-1-{i}-4.png" for i in range(1, 73)]
    gallery2_urls = [f"https://modeles3.meteociel.fr/modeles/icon2i/run/icon2i_it1-38-{i}-4.png" for i in range(1, 73)]

    # 3. Crea le due gallerie
    gallery1 = ImageGalleryWidget(galleries_container, gallery1_urls, "Galleria 1 (Pioggia)")
    gallery2 = ImageGalleryWidget(galleries_container, gallery2_urls, "Galleria 2 (Nuvole)")

    # Lista delle gallerie per un controllo più semplice
    all_galleries = [gallery1, gallery2]

    # --- 4. PANNELLO DI CONTROLLO UNIFICATO ---
    control_frame = tk.Frame(root, bg="#2E2E2E")
    control_frame.pack(pady=15)

    def go_previous_all():
        """ Funzione per mandare indietro TUTTE le gallerie. """
        for g in all_galleries:
            g.go_to_previous()
        update_controls()

    def go_next_all():
        """ Funzione per mandare avanti TUTTE le gallerie. """
        for g in all_galleries:
            g.go_to_next()
        update_controls()

    def update_controls():
        """ Aggiorna lo stato dei bottoni e dell'etichetta. """
        # Assumiamo che tutte le gallerie siano sincronizzate
        current_index = gallery1.current_image_index
        total_images = len(gallery1.urls)

        prev_button.config(state="disabled" if current_index == 0 else "normal")
        next_button.config(state="disabled" if current_index == total_images - 1 else "normal")
        info_label.config(text=f"Immagine {current_index + 1} di {total_images}")

    prev_button = tk.Button(control_frame, text="<< Precedente", command=go_previous_all, font=("Helvetica", 12), bg="#4A4A4A", fg="white", relief="flat", width=15)
    prev_button.pack(side="left", padx=20)

    info_label = tk.Label(control_frame, text="", font=("Helvetica", 14, "bold"), bg="#2E2E2E", fg="white", width=20)
    info_label.pack(side="left", padx=20)

    next_button = tk.Button(control_frame, text="Successiva >>", command=go_next_all, font=("Helvetica", 12), bg="#4A4A4A", fg="white", relief="flat", width=15)
    next_button.pack(side="left", padx=20)

    # Inizializza lo stato dei controlli (all'inizio l'etichetta è vuota)
    update_controls()

    # Avvia il loop principale
    root.mainloop()
