import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('300x400')
window.title('My Calculator')

# logic
def showNum(x):
    calc = screen_var.get()
    calc = calc + str(x)
    screen_var.set(calc)

def btnCancelFunc():
    screen_var.set(0)

def equalFunction():
    calc = screen_var.get()
    ans = eval(calc)
    screen_var.set(ans)


# Interface
screen_var = tk.StringVar()
screen = ttk.Entry(window, font='arial 14' , textvariable=screen_var)
screen.pack(side='top', fill='x', pady=10)

btnPanel = ttk.Frame(window)
btnPanel.pack()

btnNums = []
x = 0
for i in range(0, 3):       # i = 1
    for j in range(0, 3):   # j = 0
        x = x+1
        btnNums = ttk.Button(btnPanel, text=x, command=lambda val=x: showNum(val)).grid(row=i, column=j)

btnDivide = ttk.Button(btnPanel, text='/', command=lambda val=x: showNum('/')).grid(row=0, column=3)
btnMulti = ttk.Button(btnPanel, text='*', command=lambda val=x: showNum('*')).grid(row=1, column=3)
btnPlus = ttk.Button(btnPanel, text='+', command=lambda val=x: showNum('+')).grid(row=2, column=3)
btnMinus = ttk.Button(btnPanel, text='-', command=lambda val=x: showNum('-')).grid(row=3, column=3)
btnnum0 = ttk.Button(btnPanel, text='0', command=lambda val=x: showNum('0')).grid(row=3, column=0)
btnCancel = ttk.Button(btnPanel, text='C', command=btnCancelFunc).grid(row=3, column=1)
btnEqual = ttk.Button(btnPanel, text='=', command=equalFunction).grid(row=3, column=2)


# Run
window.mainloop() 