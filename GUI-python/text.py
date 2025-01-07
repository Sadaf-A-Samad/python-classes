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

    def getText(self):
        self.text.insert('1.0', 'This is text given by me. ')
      

    def getText2(self):
        # x = self.text.get('1.0', '1.5')
        x = self.text.selection_get()
        self.text1.insert('1.0', x)
        

    def interface(self):
        button = ttk.Button(self,text='click', command=self.getText).pack(pady=10)
        button2 = ttk.Button(self,text='click me', command=self.getText2).pack(pady=10)

        txtVar = tk.StringVar()
        self.text = ttk.Text(
            master=self,
            height=5,
        )
        self.text.pack()
    	
        self.text1 = ScrolledText(
            master=self,
            height=5,
        )
        self.text1.pack()

        


textWidget("My Text Widgets", 400, 400)
