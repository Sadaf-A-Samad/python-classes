import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.geometry('300x400')
window.title('My Calculator')


# logic
# def showNum(x):
#     # print(x)
#     screen_var.set(x)




# Interface
screen_var = tk.StringVar()
screen = ttk.Entry(window, font='arial 14' , textvariable=screen_var)
screen.pack(side='top', fill='x', pady=10)

btnPanel = ttk.Frame(window)
btnPanel.pack()

num0 = ttk.Button(btnPanel, text='0')
num1 = ttk.Button(btnPanel, text='1')
num2 = ttk.Button(btnPanel, text='2')
num3 = ttk.Button(btnPanel, text='3')
num4 = ttk.Button(btnPanel, text='4')
num5 = ttk.Button(btnPanel, text='5')
num6 = ttk.Button(btnPanel, text='6')
num7 = ttk.Button(btnPanel, text='7')
num8 = ttk.Button(btnPanel, text='8')
num9 = ttk.Button(btnPanel, text='9')

num0.grid(row=0, column=0)
num1.grid(row=0, column=1)
num2.grid(row=0, column=2)
num3.grid(row=0, column=3)
num4.grid(row=1, column=0)
num5.grid(row=1, column=1)
num6.grid(row=1, column=2)
num7.grid(row=1, column=3)
num8.grid(row=2, column=0)
num9.grid(row=2, column=1)

# btnNums = []
# x = 0
# for i in range(0, 3):
#     for j in range(0, 3):
#         x = x+1
#         num0 = ttk.Button(btnPanel, text=x, command=lambda val=x: showNum(val)).grid(row=i, column=j)



# Run
window.mainloop()