from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All files", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

root = Tk()

fram = Frame(root)
fram.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(fram, text="Select an image", command=showimage)
btn.pack(side=LEFT)

btn2 = Button(fram, text="Exit", command=lambda: exit())
btn2.pack(side=LEFT, padx=12)

root.title("Image Viewer")
root.geometry("400x450")
root.mainloop()
