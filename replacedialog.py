import tkinter as tk
import ttkbootstrap as ttk

class replace(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()


    def interface(self):
        frame1 = tk.Frame(self, borderwidth=10, border=tk.SUNKEN).pack(anchor=tk.CENTER)
        



replace("Replace Dialog", 400, 150)