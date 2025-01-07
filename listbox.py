import tkinter as tk
import ttkbootstrap as ttk
from tkinter.messagebox import showinfo

class listBox(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()
        self.mainloop()


    def items_selected(self,event):
            # get all selected indices
        selected_indices = self.listbox.curselection()
            # get selected items
        selected_langs = ",".join([self.listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'
        
        showinfo(title='Information', message=msg)
        print(f'item selected {msg}')


    def interface(self):
        # create a list box
        langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')
        var = tk.Variable(value=langs)
        self.listbox = tk.Listbox(
            self,
            listvariable=var,
            height=6,
            selectmode=tk.EXTENDED
        ) 
        self.listbox.bind('<<ListboxSelect>>', self.items_selected)
        self.listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

       
        # link a scrollbar to a list
        scrollbar = ttk.Scrollbar(
            self,
            orient=tk.VERTICAL,
            command=self.listbox.yview
        )

        self.listbox['yscrollcommand'] = scrollbar.set

        scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)




listBox('List box', 200, 200)