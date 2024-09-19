import tkinter as tk
import random


def lancer_de():
    r = random.randint(1,6)
    label.config(text=str(r))


window = tk.Tk()
window.title("DiceUp")

label = tk.Label(window,text="1",font=("Arial",20))
label.pack(pady=10)

button = tk.Button(window,text="Tourne le dé",command=lancer_de)
button.pack(pady=30)

window.mainloop()




