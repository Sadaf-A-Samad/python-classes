import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

class widget3(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()


    def interface(self):
        self.val1 = tk.DoubleVar()

        scale = ttk.Scale(self, 
                          command=lambda value: print(self.val1.get()), 
                          from_=0, 
                          to=100, 
                          length=300, 
                          orient='horizontal',
                          variable=self.val1
                          )
        scale.pack()


        progress = ttk.Progressbar(
            master=self,
            length=300,
            value=30,
            variable=self.val1
        )
        progress.pack(pady=20)

        spin = ttk.Spinbox(
            master=self,
            from_=1,
            to=10,
            increment=1,
            cursor='umbrella'

        )
        spin.bind('<<Increment>>', lambda event: print("Up"))
        spin.bind('<<Decrement>>', lambda event: print("Down"))
        spin.pack(pady=20)

widget3('Widget', 400, 400)