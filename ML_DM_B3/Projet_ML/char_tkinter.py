# Étape 1 : Collecte et Prétraitement des Données

# Importation des bibliothèques nécessaires
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageOps

# Classe pour l'interface utilisateur permettant de dessiner des lettres manuscrites
class HandwritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Handwriting Character Input")

        # Canevas pour dessiner
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Boutons
        self.clear_button = tk.Button(root, text="Effacer", command=self.clear_canvas)
        self.clear_button.grid(row=1, column=0)

        self.save_button = tk.Button(root, text="Enregistrer", command=self.save_drawing)
        self.save_button.grid(row=1, column=1)

        self.quit_button = tk.Button(root, text="Quitter", command=root.quit)
        self.quit_button.grid(row=1, column=2)

        # Dessin avec la souris
        self.canvas.bind("<B1-Motion>", self.paint)

        # Image PIL pour capturer les dessins
        self.image = Image.new("L", (300, 300), "white")
        self.draw = ImageDraw.Draw(self.image)

    def paint(self, event):
        x, y = event.x, event.y
        r = 5  # Rayon du pinceau
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")
        self.draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw.rectangle([0, 0, 300, 300], fill="white")

    def save_drawing(self):
        # Conversion en image binaire et enregistrement
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            # Rogner l'image pour enlever les marges blanches
            bbox = ImageOps.invert(self.image).getbbox()
            cropped_image = self.image.crop(bbox) if bbox else self.image

            # Redimensionner à une taille standard (64x64 pixels)
            resized_image = cropped_image.resize((64, 64), Image.ANTIALIAS)

            resized_image.save(filename)
            print(f"Image enregistrée sous : {filename}")

# Initialisation de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = HandwritingApp(root)
    root.mainloop()