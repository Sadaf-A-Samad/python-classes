from tkinter import *

main = Tk()
main.geometry('600x600')
main.title("Geometry Intro")
# frame1 = Frame(main, width=300, height=500)

myLabel = Label(main, text="Label Heading", bg='orange', fg='black', padx=30, pady=20)

# myLabel.pack(side='left', fill=X, fill=Y)
# myLabel.pack(fill=BOTH)

# frame1.pack()

myLabel.place(x=0,y=0, relheight=1, relwidth=0.3)

main.mainloop()