import PIL
from PIL import Image
from tkinter.filedialog import *

file_path=askopenfilename()
img=PIL.Image.open(file_path)
myheight,mywidth=img.size

img=img.resize((myheight,mywidth),PIL.Image.ANTIALIAS)
save_path=asksaveasfilename()
img.save(save_path+'Compressed.jpg')
print("Image compressed successfully..")
