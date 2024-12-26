import tkinter as tk
from tkinter import ttk, font

class widget1(tk.Tk):
    def __init__(self,title, w, h):
        super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')

        # print(font.families())
        self.interface()

        self.mainloop()

    def interface(self):
        self.style = ttk.Style(self)
        self.style.configure('TButton', foreground='red', font=('forte', 14))
        # self.style.configure('TEntry', foreground='red')
        self.style.configure('TLabel', font=('Castellar', 14))
        self.style.configure('my.TEntry', foreground='orange', padx=24)
        
        # b2 = tk.Button(self, text='TK buton', bg='orange').pack()
        l1 = ttk.Label(master=self, text='Enter some text', background="orange", foreground='white')
        l1.pack()
        e1= ttk.Entry(self, style='my.TEntry').pack()
        b1 = ttk.Button(self, text='Click me', style='').pack()



w1 = widget1('My Widget1', 400,400)
