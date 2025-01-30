import os
from PIL import ImageTk, Image
import tkinter

root = tkinter.Tk()
folder_list = os.listdir(r"C:\Users\Teknoloji\Desktop\Phyton\Jack\Selam")

def Imagen(img_path):
    img = ImageTk.PhotoImage(Image.open(f'images/{img_path}'))
    #label = tkinter.Label(image=img)
    image.whatever = img #keeping a reference, can be anything
    image.itemconfigure('image',image=img)
    image.pack()

for i in folder_list:
    button = tkinter.Button(root,text=i,command=lambda i=i:Imagen(i),width=10) 
    button.pack(pady=5)

image = tkinter.Canvas(root,width=300,height=300)
image.create_image(120,120,tag='image')

root.mainloop()