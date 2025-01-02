import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

class widget1(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()


    def clickme(self):
        self.l1.configure(
                        text='the text is changed',
                           background='orange', 
                           foreground='white'
                           )


    def interface(self): 
        # self.photo = tk.PhotoImage(file='./assets/men.png', height=100, width=100)

        self.image=Image.open('./assets/men.png')
        self.img=self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.img)

        self.l1 = ttk.Label(master=self, text='Enter some text',
                             font=('Palace Script MT', 24), 
                             padding= 10,
                             image=self.photo,
                             compound='top'
                                               
                             )
        self.l1.pack(padx=10, pady=10)

        e1 = ttk.Entry(master=self)
        e1.pack(padx=10, pady=10)
       
        b1 = ttk.Button(master=self, text='Click me', 
                        command=self.clickme, 
                        image=self.photo, 
                        compound='left')
        b1.pack(padx=10, pady=10)



w1 = widget1('My Widget1', 400,400)
