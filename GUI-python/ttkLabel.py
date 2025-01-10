
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# show a label
# label = ttk.Label(master, **options)

label = ttk.Label(
    root,
    text='A Label with the Helvetica font',
    font=("Helvetica", 14))

label.pack(ipadx=10, ipady=10)

# display an image label
# photo = tk.PhotoImage(file='./assets/men.png', width=100, height=100)
# image_label = ttk.Label(
#     root,
#     image=photo,
#     text='Python',
#     compound='top',
#     justify='center'
# )

# Image load from pillow library
# ----------- pip install Pillow
# Load the image
image=Image.open('./assets/men.png')

# Resize the image in the given (width, height)
img=image.resize((100, 100))

photo = ImageTk.PhotoImage(img)
image_label = ttk.Label(
    root,
    image=photo,
    text='Python',
    compound='top',
    justify='center'
)

image_label.pack()
root.mainloop()

