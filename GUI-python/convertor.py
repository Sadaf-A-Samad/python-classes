import tkinter as tk
from tkinter import ttk

# window
root = tk.Tk()
root.geometry('250x150')
root.title("My Convertor")

# Logic

def convert():
    x = input_var.get()
    print(f"This is Convert Button {x}")
    con = x*100
    output_var.set(con)


# interface
title_label = ttk.Label(master=root, text='Convert meter to cm', font='arial 14 bold', padding='10')
title_label.pack()

input_frame = ttk.Frame(root, padding=10)
input_frame.pack()

input_var = tk.DoubleVar()
entry_convert = ttk.Entry(input_frame, textvariable=input_var)
entry_convert.grid(row=0, column=0)

btn_convert = ttk.Button(input_frame, text='Convert', command=convert)
btn_convert.grid(row=0, column=1)

output_var = tk.StringVar()
lbl_output = ttk.Label(root, text='Show Result', font='arial 14 bold', padding=10, textvariable=output_var)
lbl_output.pack()


# Run 
root.mainloop()