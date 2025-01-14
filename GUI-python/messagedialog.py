import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog, simpledialog
# from tkinter import messagebox

class menuWidget(ttk.Window):
    def __init__(self,title, w, h):
        super().__init__()
        
        self.title(title)
        self.geometry(f'{w}x{h}')

        self.interface()

        self.mainloop()


    def interface(self):

         # Create a text widget
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        # Create a menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Create a file menu
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save",)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.destroy)

        # Create an edit menu
        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", )
        edit_menu.add_command(label="Copy", )
        edit_menu.add_command(label="Paste", )


    
    def new_file(self):
        # x = tk.messagebox.showinfo("Show Info", "YOur Data is Saved")
        # x = tk.messagebox.showwarning("Show Warning", "Do you Want to submit")
        # x = tk.messagebox.showerror("Show Error", "Do you Want to submit")
        # x = tk.messagebox.askquestion("Ask Question", "Do you Want to submit", icon="question")
        # x = tk.messagebox.askokcancel("Ask Question", "Do you Want to submit", icon="info")
        # x = tk.messagebox.askyesno("Ask Question", "Do you Want to submit", icon='warning')
        # x = tk.messagebox.askretrycancel("Ask Question", "Do you Want to submit", icon="error")
        x = tk.messagebox.askyesnocancel("Ask Question", "Do you want to save this file?")
        # print(x)
        if x==True:
            self.save_file()
        elif x == False:
            self.text.delete("1.0", "end")
            self.title("Untitled - Notepad")
        

    
    def open_file(self):
        # val = tk.simpledialog.askstring("title", "Enter value")
        # val = tk.simpledialog.askfloat("title", "Enter value")
        # val = tk.simpledialog.askinteger("title", "Enter value")
        # print(val)
        # file = tk.filedialog.askopenfiles(parent=self, mode="rb", title="Open a file")
        # file = tk.filedialog.askdirectory(parent=self, mode="rb", title="Open a file")
        x = tk.messagebox.askyesnocancel("Ask Question", "Do you want to save this file?")
        if x==True:
            self.save_file()
        elif x == False:
            file = tk.filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
            if file:
                contents = file.read()
                self.text.delete("1.0", "end")
                self.text.insert("1.0", contents)
                file.close()
                self.title(file.name + " - Notepad")


    def save_file(self):
        x = tk.messagebox.askyesno("Ask Question", "Do you want to save this file?")
        if x==True: 
            file = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
            if file:
                contents = self.text.get("1.0", "end")
                file.write(contents)
                file.close()
                self.title(file.name + " - Notepad")
        
        
menuWidget("My Menu", 400, 400)