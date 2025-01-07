import tkinter as tk
import ttkbootstrap as ttk
from tkinter.messagebox import showinfo

class checkbox_widget(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()


    def agreement_changed(self):
        tk.messagebox.showinfo(title='Result',
                                message=self.agreement.get())

    def interface(self):
        self.agreement = tk.StringVar()
        chk1 = ttk.Checkbutton(self,
                text='I agree',
                command=self.agreement_changed,
                variable=self.agreement,
                onvalue='agree',
                offvalue='disagree').pack()
       
        chk2 = ttk.Checkbutton(self,
                text='I agree',
                command=self.agreement_changed,
                
                onvalue='agree',
                offvalue='disagree').pack()


checkbox_widget("My checkbox Widgets", 400, 400)
