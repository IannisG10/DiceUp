import tkinter as tk
import random

def display_faces(canvas, nombre):
    canvas.delete("All")
    rayon = 5

    # Declaration des positions des points du dé
    positions = [
        (50, 50),
        (25, 25),
        (75, 75),
        (25, 75),
        (75, 25),
        (50, 25),
        (50, 75)
    ]

    # Declaration d' un Dictionnaire pour stocker les positions d' une face
    faces = {

    }



# creation de la fetenetre Tkinter
window = tk.Tk()
window.title("DiceUp")
window.geometry("400x300")