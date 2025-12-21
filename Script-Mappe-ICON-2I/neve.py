import tkinter as tk
from tkinter import messagebox, ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import threading

# --- GENERAZIONE DINAMICA DEGLI URL ---
base_url = "https://modeles3.meteociel.fr/modeles/icon2i/run/icon2i_it1-45-{}-4.png"
image_urls = [base_url.format(i) for i in range(1, 73)]

class ImageGallery:
    def __init__(self, root, urls):
        self.root = root
        self.urls = urls
        self.images = [None] * len(urls)
        self.current_image_index = 0

        # --- Impostazioni della finestra (adattata per 768x768 px + controlli) ---
        self.root.title("Galleria Immagini Meteo (Risoluzione Originale)")
        self.root.geometry("800x850") # Finestra più grande per contenere l'immagine
        self.root.configure(bg="#2E2E2E")

        # --- Frame per il caricamento ---
        self.loading_frame = tk.Frame(root, bg="#2E2E2E")
        self.loading_frame.pack(pady=20)
        self.loading_label = tk.Label(self.loading_frame, text="Caricamento immagini...", font=("Helvetica", 14), bg="#2E2E2E", fg="white")
        self.loading_label.pack()
        self.progress_bar = ttk.Progressbar(self.loading_frame, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        # --- Frame principale (inizialmente nascosto) ---
        self.main_frame = tk.Frame(root, bg="#2E2E2E")

        self.image_label = tk.Label(self.main_frame, bg="#2E2E2E")
        self.image_label.pack(expand=True, fill="both", padx=10, pady=10)

        self.info_label = tk.Label(self.main_frame, text="", font=("Helvetica", 10), bg="#2E2E2E", fg="white")
        self.info_label.pack()

        button_frame = tk.Frame(self.main_frame, bg="#2E2E2E")
        button_frame.pack(pady=10)

        self.prev_button = tk.Button(button_frame, text="<< Precedente", command=self.show_previous_image, font=("Helvetica", 12), bg="#4A4A4A", fg="white", relief="flat")
        self.prev_button.pack(side="left", padx=10)

        self.next_button = tk.Button(button_frame, text="Successiva >>", command=self.show_next_image, font=("Helvetica", 12), bg="#4A4A4A", fg="white", relief="flat")
        self.next_button.pack(side="right", padx=10)

        self.loading_thread = threading.Thread(target=self.load_images)
        self.loading_thread.start()

    def load_images(self):
        """ Scarica e carica le immagini senza modificarne la risoluzione. """
        total_images = len(self.urls)
        for i, url in enumerate(self.urls):
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()

                # --- CARICAMENTO IMMAGINE SENZA RIDIMENSIONAMENTO ---
                # Apriamo l'immagine e la usiamo così com'è.
                img = Image.open(BytesIO(response.content))

                # Convertiamo direttamente l'immagine originale per Tkinter.
                self.images[i] = ImageTk.PhotoImage(img)
                # ----------------------------------------------------

                progress = (i + 1) / total_images * 100
                self.progress_bar['value'] = progress

            except requests.exceptions.RequestException as e:
                print(f"Errore nel scaricare l'immagine {i+1}: {e}")
            except Exception as e:
                print(f"Errore generico sull'immagine {i+1}: {e}")

        self.root.after(0, self.show_main_interface)

    def show_main_interface(self):
        self.loading_frame.pack_forget()
        self.main_frame.pack(expand=True, fill="both")

        if not any(self.images):
            messagebox.showerror("Errore", "Nessuna immagine caricata.")
            self.root.destroy()
        else:
            self.show_image()

    def show_image(self):
        if self.images[self.current_image_index]:
            current_tk_image = self.images[self.current_image_index]
            self.image_label.config(image=current_tk_image)
            self.image_label.image = current_tk_image
        else:
            self.image_label.config(text=f"Immagine {self.current_image_index + 1} non disponibile", image='')

        self.info_label.config(text=f"Immagine {self.current_image_index + 1} di {len(self.urls)}")
        self.update_buttons()

    def show_previous_image(self):
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_image()

    def show_next_image(self):
        if self.current_image_index < len(self.images) - 1:
            self.current_image_index += 1
            self.show_image()

    def update_buttons(self):
        self.prev_button.config(state="disabled" if self.current_image_index == 0 else "normal")
        self.next_button.config(state="disabled" if self.current_image_index == len(self.images) - 1 else "normal")


if __name__ == "__main__":
    main_window = tk.Tk()
    gallery_app = ImageGallery(main_window, image_urls)
    main_window.mainloop()
