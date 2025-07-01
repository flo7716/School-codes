import customtkinter as ctk
from tkinter import Canvas
from PIL import Image, ImageDraw, ImageOps

# Configuration de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LetterDatasetApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dataset de Lettres")
        self.geometry("800x600")

        # Variables
        self.letter_name = ctk.StringVar()
        self.canvas_width = 512
        self.canvas_height = 512
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Zone de dessin
        self.canvas = Canvas(self, bg="white", width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.canvas.bind("<B1-Motion>", self.draw_on_canvas)

        # Champ pour saisir la lettre
        self.letter_label = ctk.CTkLabel(self, text="Lettre :")
        self.letter_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.letter_entry = ctk.CTkEntry(self, textvariable=self.letter_name)
        self.letter_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        # Boutons
        self.save_button = ctk.CTkButton(self, text="Sauvegarder", command=self.save_image)
        self.save_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_button = ctk.CTkButton(self, text="Effacer", command=self.clear_canvas)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)

    def draw_on_canvas(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black", outline="black")
        self.draw.ellipse([x-2, y-2, x+2, y+2], fill="black")

    def save_image(self):
        letter = self.letter_name.get().strip()
        if not letter:
            ctk.CTkMessagebox.show_warning("Erreur", "Veuillez entrer une lettre.")
            return

        # Sauvegarder l'image redimensionnée
        output_image = self.image.copy()
        output_image = ImageOps.fit(output_image, (512, 512), method=Image.Resampling.LANCZOS)
        output_image.save(f"{letter}.png")
        ctk.CTkMessagebox.show_info("Succès", f"L'image '{letter}.png' a été sauvegardée.")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    app = LetterDatasetApp()
    app.mainloop()
