import tkinter as tk
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg='white', width=200, height=200)
        self.canvas.pack()
        self.image = Image.new("L", (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)
        self.canvas.bind("<B1-Motion>", self.paint)
        
        # Bouton pour sauvegarder l'image et effacer le canevas
        self.save_button = tk.Button(root, text="Enregistrer", command=self.save_image)
        self.save_button.pack()
        self.clear_button = tk.Button(root, text="Effacer", command=self.clear_canvas)
        self.clear_button.pack()

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x+5, y+5, fill='black', width=5)
        self.draw.ellipse([x, y, x+5, y+5], fill='black')

    def save_image(self):
        self.image = self.image.resize((28, 28))
        self.image.save("lettre_a_predire.png")
        print("Image enregistrée pour reconnaissance.")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (200, 200), 'white')
        self.draw = ImageDraw.Draw(self.image)

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
