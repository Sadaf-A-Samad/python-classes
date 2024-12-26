from tkinter import *

root = Tk()


label1 = Label(root, text ='This is my first label...')
label1 = Label(root, text ='This is my first label...')
label2 = Label(root, text ='This is my Second label...').grid(row=0, column=1)

# label1.pack()
label1.grid(row=0, column=0)
print('hello')


root.mainloop()