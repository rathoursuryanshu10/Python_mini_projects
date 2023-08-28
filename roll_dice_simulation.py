import tkinter as tk
from PIL import Image,ImageTk
import random as rn



window=tk.Tk()
window.geometry("500x400")
window.title("Dice Roll")
"""
def roll_dice():
    a=rn.randint(1,6)
    label=tk.Label(window,text=a).pack()

button = tk.Button(window,text="Click to roll",command=roll_dice)
button.pack()
"""

dice=["one.png", "two.png", "three.png","four.png", "five.png", "six.png"]
image1=ImageTk.PhotoImage(Image.open(rn.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(rn.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image=image1
label2.image=image2

label1.place(x=30,y=100)
label2.place(x=270,y=100)
def roll_dice():
    image1=ImageTk.PhotoImage(Image.open(rn.choice(dice)))
    label1.configure(image=image1)
    label1.image=image1

    image2=ImageTk.PhotoImage(Image.open(rn.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2

button = tk.Button(window,text="Roll dice ",bg="blue",fg="white", font="bold", command=roll_dice)
button.place(x=200,y=350)
window.mainloop()
