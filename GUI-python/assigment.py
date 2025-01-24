import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymongo

class utility(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="cyborg")
        self.title(title)
        self.geometry(f'{w}x{h}')
       
    
        self.interface()     
        self.mainloop()
    
    def interface(self):
        label=ttk.Label(self,text='utility store main page',font=('Algerian',15),background='blue')
        label.pack(fill='both')

        label2=ttk.Label(self,text='welcome Abdullah',font=('bold',10),background='grey')
        label2.pack(fill='both')
        myframe=ttk.Frame(self,)
        myframe.pack()

        label3=ttk.Label(myframe,text='employes',background='orange')
        label3.pack(padx=20,pady=50,fill='x')

        
utility('utility page',500,500)