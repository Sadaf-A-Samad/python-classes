from tkinter import *

root = Tk()

root.geometry('400x400')
root.minsize(200,100)
root.maxsize(600, 600)


loginHeading = Label(root, text="Login Form", fg='orange', bg='grey', font='forte 18 bold', padx=7, pady=15,)

lblUsername = Label(text='Username').grid(row=2,column=0)
txtUsername = Text(height=1, width=24).grid(row=2, column=2)
lblPassword = Label(text='Password').grid(row=3, column=0)
txtUsername = Text(height=1, width=24).grid(row=3, column=2)

btnLogin = Button(text="Login").grid(row=5, column=1)

loginHeading.grid(row=0, column=0, columnspan=3)

root.mainloop()