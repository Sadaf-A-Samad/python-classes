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


    def show_combo_value(self, event):
        # print('hello')
        print(self.comboVar.get())


    def checkEvent(self, event):
        print('Event Called')



    def checkEvent(self, event):
        print('Event Called: ', event.x, event.y)


    def interface(self):

        mylist = ['Pakistan', 'USA', 'China', 'Japan']
        self.comboVar = tk.StringVar(value = mylist[0])
        mycombo = ttk.Combobox(self, textvariable = self.comboVar)
        mycombo.configure(values=mylist)
        mycombo.pack()

        mycombo.bind('<<ComboboxSelected>>', self.show_combo_value)


        button = ttk.Button(self, text='check events').pack(pady=15)

        mycombo.bind('<Alt-KeyPress-a>', self.checkEvent)

        mycombo.bind('<Double-Button-1>', self.checkEvent)

        self.bind('<Motion>', self.checkEvent)

w1 = widget1('Combo Box', 400,400)