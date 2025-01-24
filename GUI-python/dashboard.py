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


    def config(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client["tiictsystem"]
        print("Connected to Mongodb: ", self.db)


    def signup(self):
        mycollection = self.db["users"]
        user = self.username.get()
        password = self.password.get()
        email = self.email.get()

        doc = {
            'username': user,
            'password': password,
            'email': email
        }
        user1 = mycollection.insert_one(doc)
        if user1:
            print("user is created")
            tk.messagebox.showinfo("Show Info", "New User created")


    def loadImage(self, img):
        pass
        

    def imgComponent(self, img, label, r, c):
        image1=Image.open(img)
        img1=image1.resize((150, 150))
        self.photo1 = ImageTk.PhotoImage(img1)
       

        l1 = ttk.Label(master=self.container, 
                             padding= 10,
                             image=self.photo1,
                             text=label,
                             compound="top"                                               
                             )
        l1.grid(row=r, column=c,padx=10, pady=10)


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

        self.imgComponent('./assets/bike.png', "Total Students", 0,0)
        self.imgComponent('./assets/car.png', "Total Teachers", 0,1)
        self.imgComponent('./assets/bike.png', "Total Users", 1,0)
        self.imgComponent('./assets/dino.png', "Total Users", 1,1)
       

        

        


      

      

dashboard("Dashboard - SMS", 600, 300)