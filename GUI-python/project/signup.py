import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from config import DBConnect	 

class signup(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="cyborg")
        self.title(title)
        self.geometry(f'{w}x{h}')
       
        DBConnect.configDB(self) 
        self.interface()     
        self.mainloop()


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



    def interface(self):
        self.password = tk.StringVar()
        self.username = tk.StringVar()
        self.email = tk.StringVar()


        lbl_title = ttk.Label(self, 
                              text="Register User", 
                              font=('Poor Richard', 24)
                              )
        lbl_title.pack(pady=15, padx=15)

        my_frame2 = ttk.Frame(self)
        my_frame2.pack(padx=10, pady=10, side="left")


        self.image=Image.open('./assets/login.png')
        self.img=self.image.resize((250, 250))
        self.photo = ImageTk.PhotoImage(self.img)

        self.l1 = ttk.Label(master=my_frame2, 
                             padding= 10,
                             image=self.photo,                                               
                             )
        self.l1.pack(padx=10, pady=10)

        my_frame = ttk.Frame(self)
        my_frame.pack(padx=10, pady=10, side="right")

        
        lbl_user = ttk.Label(my_frame, text="Enter Username")
        lbl_user.grid(column=1,row=1, pady=5,padx=5)
        entry_user = ttk.Entry(my_frame, textvariable=self.username)
        entry_user.grid(column=2,row=1, pady=5, padx=5)


        lbl_pass = ttk.Label(my_frame, text="Enter Password")
        lbl_pass.grid(column=1,row=2, pady=5,padx=5)
        entry_pass = ttk.Entry(my_frame, textvariable=self.password, show="*")
        entry_pass.grid(column=2,row=2, pady=5, padx=5)


        lbl_email = ttk.Label(my_frame, text="Enter Email")
        lbl_email.grid(column=1,row=3, pady=5,padx=5)
        entry_email = ttk.Entry(my_frame, textvariable=self.email)
        entry_email.grid(column=2,row=3, pady=5, padx=5)

        btn_register = ttk.Button(my_frame, text="Register", 
                                  command=self.signup,
                                  bootstyle='success outline ')
        btn_register.grid(column=1, row=4, pady=5, padx=5)
        btn_cancel = ttk.Button(my_frame, text="Cancel", bootstyle='danger')
        btn_cancel.grid(column=2, row=4, pady=15, padx=10)

signup("Register User", 600, 300)