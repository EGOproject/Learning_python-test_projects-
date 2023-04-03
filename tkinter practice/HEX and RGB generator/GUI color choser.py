#this is a color selector that allows one to know the RGB or Hex value of the color they want
#can come in handy while using CSS and HTML also py gui projects
#credit: EGOproject

from tkinter import *
from tkinter import colorchooser
import os

root = Tk()
root.title("GUI color selector")
root.iconbitmap("tkinter practice/favicon/favicon.ico")
# root.geometry("300x300")

def select():
    color = colorchooser.askcolor()
    
    #rgb alogarithm
    rgb = []
    for value in color:
        rgb.append(value)
    
    color_rgb = f"{rgb[0][0]},{rgb[0][1]},{rgb[0][2]}"

    rgb_screen.delete(0, END)
    rgb_screen.insert(0, color_rgb)
    color_hex = color[1]
    hex_screen.delete(0, END)
    hex_screen.insert(0, color_hex)

    root.config(bg=color_hex)
    
def copy_rgb_values():
    text = f"{rgb_screen.get()}"
    copy = 'echo ' + text.strip() + '| clip'
    os.system(copy)

def copy_hex_values():
    text = f"{hex_screen.get()}"
    copy = 'echo ' + text.strip() + '| clip'
    os.system(copy)
    

header_label = Label(root, text="Hex and RGB Generator", bg="white", fg="black").grid(row=0, column=0, columnspan=3, padx=10, pady=10)

rgb_label = Label(root, text="R G B", bg="white", fg="black").grid(row=1, column=0, padx=10, pady=10)
rgb_screen = Entry(root, width=30)
rgb_screen.grid(row=1, column=1, padx=10, pady=10 )
rgb_copy = Button(root, text="Copy RGB", bg="white", fg="black", command=copy_rgb_values).grid(row=1, column=2, padx=10, pady=10)

hex_label = Label(root, text="H E X", bg="white", fg="black").grid(row=2, column=0, padx=10, pady=10)
hex_screen = Entry(root, width=30)
hex_screen.grid(row=2, column=1, padx=10, pady=10 )
hex_copy = Button(root, text="Copy HEX", bg="white", fg="black", command=copy_hex_values).grid(row=2, column=2, padx=10, pady=10)
Button(root, text="Select color", bg="white", fg="black", command=select).grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()