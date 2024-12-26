import tkinter as tk
import ttkbootstrap as ttk

class widget1(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="vapor")
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()

    def interface(self):
         
        l1 = ttk.Label(master=self, text='Enter some text')
        l1.pack()
        e1= ttk.Entry(self, style='my.TEntry')
        e1.pack()
        b1 = ttk.Button(self, text='Click me')
        b1.pack()



w1 = widget1('My Widget1', 400,400)
