import tkinter as tk
import ttkbootstrap as ttk

class widget1(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__(themename="darkly")
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()



    def interface(self):
        myframe = ttk.Frame(master=self).pack()
         
        l1 = ttk.Label(self, text='Enter some text').pack()
        # l1.grid(row=1, column=1)
        self.numVar = tk.StringVar()
        self.tabVar = tk.StringVar()
        e1= ttk.Entry(master=self, textvariable=self.numVar).pack()
        # e1.grid(row=1, column=1)
        b1 = ttk.Button(master=self, text='Click me', command=self.showTable).pack()
        # b1.grid(row=1, column=1)
        t1 = ttk.Text(master=self, ).pack()
        # t1.insert('end', self.tabVar)



    def showTable(self):
        x = self.numVar.get()
        self.tabVar.set(x)
        print("Button is clicked")



w1 = widget1('My Widget1', 400,400)
