import tkinter as tk
import ttkbootstrap as ttk
from tkinter.messagebox import showinfo

class radioWidget(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()

        


    def show_selected_size(self):
        tk.messagebox.showinfo(title='Result',
                                message=self.selected_size.get())

    def interface(self):
        self.selected_size = tk.StringVar()
        sizes = (('Small', 'S'),
         ('Medium', 'M'),
         ('Large', 'L'),
         ('Extra Large', 'XL'),
         ('Extra Extra Large', 'XXL'))

            # label
        label = ttk.Label(text="What's your t-shirt size?")
        label.pack(fill='x', padx=5, pady=5)

            # radio buttons
        for size in sizes:
                r = ttk.Radiobutton(
                    self,
                    text=size[0],
                    value=size[0],
                    variable=self.selected_size
                )
                r.pack(fill='x', padx=5, pady=5)

            # button
        button = ttk.Button(
                self,
                text="Get Selected Size",
                command=self.show_selected_size)

        button.pack(fill='x', padx=5, pady=5)


radioWidget("My Radio Widgets", 400, 400)
