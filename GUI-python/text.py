import tkinter as tk
import ttkbootstrap as ttk
from tkinter.scrolledtext import ScrolledText

class textWidget(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()


    def interface(self):
        
        text = ttk.Text(
            master=self,
            height=5
        )
        text.pack()
    	
        text1 = ScrolledText(
            master=self,
            height=5
        )
        text1.pack()


textWidget("My Text Widgets", 400, 400)
