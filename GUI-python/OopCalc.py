import tkinter as tk
from tkinter import ttk

class Calc(tk.Tk):
    def __init__(self, title, w, h):
        super().__init__()
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()

       
       
        # --------Interface

    def interface(self):
        self.screen_var = tk.StringVar()
        screen = ttk.Entry(master=self, font='arial 14' , textvariable=self.screen_var)
        screen.pack(side='top', fill='x', pady=10)

        btnPanel = ttk.Frame(self)
        btnPanel.pack()

        x = 0
        for i in range(0, 3):       
            for j in range(0, 3):   
                x = x+1
                self.btns(btnPanel, x, i,j)

        self.btns(btnPanel, '/', 0,3)
        self.btns(btnPanel, '*', 1,3)
        self.btns(btnPanel, '+', 2,3)
        self.btns(btnPanel, '-', 3,3)
        self.btns(btnPanel, '0', 3,0)
        btnCancel = ttk.Button(btnPanel, text='C', command=self.btnCancelFunc)
        btnCancel.grid(row=3, column=1)
        btnEqual = ttk.Button(btnPanel, text='=', command=self.equalFunction)
        btnEqual.grid(row=3, column=2)


    def showNum(self, x):
        calc = self.screen_var.get()
        calc = calc + str(x)
        self.screen_var.set(calc)

    def btns(self, panel, t, r, c):
        btn = ttk.Button(panel, text=t, command=lambda val=t: self.showNum(val))
        btn.grid(row=r, column=c)

    def btnCancelFunc(self):
        self.screen_var.set(0)

    def equalFunction(self):
        calc = self.screen_var.get()
        ans = eval(calc)
        self.screen_var.set(ans)

Calc('My Calculator', 250, 300)