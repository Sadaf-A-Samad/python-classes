import customtkinter as ctk

class widget1(ctk.CTk):
    def __init__(self,title, w, h):
        super().__init__()
        ctk.set_default_color_theme("green")
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()



    def interface(self):
         
        l1 = ctk.CTkLabel(master=self, text='Enter some text', pady=5)
        l1.pack()
        e1= ctk.CTkEntry(master=self)
        e1.pack()
        b1 = ctk.CTkButton(master=self, text='Click me')
        b1.pack()



w1 = widget1('My Widget1', 400,400)
