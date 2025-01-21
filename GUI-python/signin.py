import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymongo

class signin(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="cyborg")
        self.title(title)
        self.geometry(f'{w}x{h}')
       
        self.config()
        self.interface()     
        self.mainloop()


    def config(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = client["tiictsystem"]
        print("Connected to Mongodb: ", self.db)


    def signin(self):
        mycollection = self.db["users"]
        email = self.email.get()
        password = self.password.get()

        doc = {
            'password': password,
            'email': email
        }
        user1 = mycollection.find_one(doc)
        if user1:
            print("Login Successfull: ",user1)
            tk.messagebox.showinfo("Show Info", f"Login Successful, Welcome Mr. {user1['username']}")



    def interface(self):
        self.password = tk.StringVar()
        self.username = tk.StringVar()
        self.email = tk.StringVar()


        lbl_title = ttk.Label(self, 
                              text="Login User", 
                              font=('Poor Richard', 24)
                              )
        lbl_title.pack(pady=15, padx=15)

        my_frame = ttk.Frame(self)
        my_frame.pack(padx=10, pady=10)


        lbl_email = ttk.Label(my_frame, text="Enter Email")
        lbl_email.grid(column=1,row=1, pady=5,padx=5)
        entry_email = ttk.Entry(my_frame, textvariable=self.email)
        entry_email.grid(column=2,row=1, pady=5, padx=5)

        lbl_pass = ttk.Label(my_frame, text="Enter Password")
        lbl_pass.grid(column=1,row=2, pady=5,padx=5)
        entry_pass = ttk.Entry(my_frame, textvariable=self.password)
        entry_pass.grid(column=2,row=2, pady=5, padx=5)


        btn_register = ttk.Button(my_frame, text="Register", 
                                  command=self.signin,
                                  bootstyle='success outline ')
        btn_register.grid(column=1, row=4, pady=5, padx=5)
        btn_cancel = ttk.Button(my_frame, text="Cancel", bootstyle='danger')
        btn_cancel.grid(column=2, row=4, pady=15, padx=10)

signin("Register User", 300, 300)