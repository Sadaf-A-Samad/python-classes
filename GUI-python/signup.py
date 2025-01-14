import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

class signup(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()


    def interface(self):
        lbl_title = ttk.Label(self, 
                              text="Register User", 
                              font=('Poor Richard', 24)
                              )
        lbl_title.pack(pady=15, padx=15)

        my_frame = ttk.Frame(self)
        my_frame.pack(padx=10, pady=10)

        lbl_user = ttk.Label(my_frame, text="Enter Username")
        lbl_user.grid(column=1,row=1, pady=5,padx=5)
        entry_user = ttk.Entry(my_frame)
        entry_user.grid(column=2,row=1, pady=5, padx=5)


        lbl_pass = ttk.Label(my_frame, text="Enter Password")
        lbl_pass.grid(column=1,row=2, pady=5,padx=5)
        entry_pass = ttk.Entry(my_frame)
        entry_pass.grid(column=2,row=2, pady=5, padx=5)


        lbl_email = ttk.Label(my_frame, text="Enter Password")
        lbl_email.grid(column=1,row=3, pady=5,padx=5)
        entry_email = ttk.Entry(my_frame)
        entry_email.grid(column=2,row=3, pady=5, padx=5)

        btn_register = ttk.Button(my_frame, text="Register")
        btn_register.grid(column=1, row=4, pady=5, padx=5)
        btn_cancel = ttk.Button(my_frame, text="Cancel")
        btn_cancel.grid(column=2, row=4, pady=15, padx=10)

signup("Register User", 300, 300)