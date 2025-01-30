import tkinter as tk
from PIL import ImageTk

# --- functions ---

def create_button(all_files, filename, row):
    # self.myImage = ImageTk.PhotoImage(Image.open(img).resize((100,100)))
    all_files.append(filename)
    button_image = ImageTk.PhotoImage(file=all_files[-1])
    button = tk.Button(app, image=button_image, border='0')
    button.img = button_image # solution for bug with PhotoImage
    button.grid(row=row, column=0, columnspan=4, ipadx=0)

# --- main ---

all_files = []

app = tk.Tk()

create_button(all_files, "./assets/bike.png", 6)
create_button(all_files, "./assets/dino.png", 8)

app.mainloop()