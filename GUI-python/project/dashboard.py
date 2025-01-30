import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymongo

class dashboard(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="cyborg")
        # super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')
       
        self.config()
        self.interface()     
        self.mainloop()



    def interface(self):
        self.password = tk.StringVar()
        self.username = tk.StringVar()
        self.email = tk.StringVar()


        lbl_title = ttk.Label(self, 
                              text="Dashboard", 
                              font=('Poor Richard', 24)
                              )
        lbl_title.pack(pady=15, padx=15)

        titlebar = ttk.Frame(self)
        titlebar.pack(padx=10, pady=10, side="top")

        sidebar = ttk.Frame(self)
        sidebar.pack(padx=10, pady=10, side="left")

        btn = ttk.Button(sidebar, text="Users", bootstyle="warning")
        btn.pack(padx=10, pady=10, fill="x")

        btn = ttk.Button(sidebar, text="Users", bootstyle="warning")
        btn.pack(padx=10, pady=10, fill="x")
        
        self.container = ttk.Frame(self)
        self.container.pack(padx=10, pady=10, side="right")
        
        imgList = ["bike.png", "car.png", "tree.png", "dino.png"]
        buttonList = ["Total Student", "Total Teacher", "Total Users", "Total Users2"]
        self.myImage = []
        
        n = 0
        for i in range(0, 2):
            for j in range(0, 2):
                self.myImage.append(ImageTk.PhotoImage(Image.open(f'./assets/{imgList[n]}').resize((100,100))))
                l1 = ttk.Button(master=self.container, 
                                padding= 10,
                                image=self.myImage[n],
                                text=buttonList[n],
                                compound="top"                                               
                                )
                l1.grid(row=i, column=j, padx=10, pady=10)
                n=n+1

        

        


      

      

dashboard("Dashboard - SMS", 600, 300)