import os
import tkinter as tk
from PIL import Image, ImageTk

# Définir le chemin du dossier contenant les images
image_folder = './images'

# Créer une fenêtre principale
root = tk.Tk()
root.title('Image Viewer')

# Créer un canevas pour afficher les images
canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Créer une variable pour stocker l'index de l'image courante
image_index = 0

# Charger la première image et la redimensionner pour qu'elle s'adapte au canevas
imgnames = os.listdir(image_folder)
images = [Image.open(os.path.join(image_folder, img)) for img in imgnames]
image = images[image_index].resize((canvas_width, canvas_height), Image.ADAPTIVE)
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)


def add_var(var, lbl):
    chk = tk.Checkbutton(root, text=lbl, variable=var)
    chk.pack()

nature_var = tk.BooleanVar()
add_var(nature_var, 'nature')
old_var = tk.BooleanVar()
add_var(old_var, 'old')
modern_var = tk.BooleanVar()
add_var(modern_var, 'modern')
classy_var = tk.BooleanVar()
add_var(classy_var, 'classy')
architecture_var = tk.BooleanVar()
add_var(architecture_var, 'architecture')

# Définir une fonction pour afficher l'image suivante et la redimensionner pour qu'elle s'adapte au canevas
def next_image():
    global imgnames, image_index, image_tk, nature_var, old_var, modern_var, classy_var, architecture_var
    tags = []
    if nature_var.get(): tags.append('nature')
    if old_var.get(): tags.append('old')
    if modern_var.get(): tags.append('modern')
    if classy_var.get(): tags.append('classy')
    if architecture_var.get(): tags.append('architecture')
    with open('./user_input/'+imgnames[image_index]+'.txt', 'w') as fi:
        fi.write(" ".join(tags))
    nature_var.set(False)
    old_var.set(False)
    modern_var.set(False)
    classy_var.set(False)
    architecture_var.set(False)
    image_index = (image_index + 1) % len(images)
    image = images[image_index].resize((canvas_width, canvas_height), Image.ADAPTIVE)
    image_tk = ImageTk.PhotoImage(image)
    canvas.delete('all')
    canvas.create_image(0, 0, image=image_tk, anchor=tk.NW)
button = tk.Button(root, text='Next Image', command=next_image)
button.pack()


# Démarrer la boucle principale de l'interface graphique
root.mainloop()
