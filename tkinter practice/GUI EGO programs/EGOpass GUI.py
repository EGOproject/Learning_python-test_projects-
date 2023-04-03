from tkinter import *
from tkinter.font import  Font
import os
import random

root= Tk()
root.title("EGO Password Generator")
root.iconbitmap("tkinter practice/GUI EGO programs/favicon/favicon.ico")
# root.geometry("400x200") 
text_font = Font(size = 15)

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!@#$%/\<>?:"
pform = upper + lower + number + symbols

password = []
def generate():
    password.clear()
    gps_screen.delete(0, END)
    plen = int(plen_screen.get())
    while plen > len(password):
        pchar = random.choice(pform)
        password.append(pchar)
    pss = "".join(password)
    gps_screen.insert(0, pss )

def copy_password():
    text = f"{gps_screen.get()}"
    copy = 'echo ' + text.strip() + '| clip'
    os.system(copy)
    

head_label = Label(root, text="Password Requirements!")
section = Label(root, text="=================================================")
plen_label = Label(root, text="Password Length [Minimum: 8]: " )
plen_screen = Entry(root, text="8", width=20, borderwidth=1)
gps_screen = Entry(root, width=50, borderwidth=5)
gen_btn = Button(root, text="Generate Password", padx=5, pady=5, bg="black", fg="white", command=generate)
space = Label(root, text="=================================================")
copy = Button(root, text="Copy", command = copy_password, padx=10, pady=5,bg="black", fg="white")

head_label.grid(column=0, row=0, columnspan=5)
plen_label.grid(column=2, row=2)
section.grid(row=1, columnspan=5)
plen_screen.grid(column=3, row=2)
gen_btn.grid(column=0, row=4, columnspan=5)
space.grid(column=0, row=3, columnspan=5)
gps_screen.grid(column=0, columnspan=4, row=6)
space.grid(column=0, row=5, columnspan=5)
copy.grid(column=4, row=6)

head_label["font"] = text_font

root.mainloop()