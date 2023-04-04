import os
import pyshorteners
from tkinter import *
from tkinter.font import  Font

root= Tk()
root.title("Link Shortener")
root.iconbitmap("tkinter practice/URL Shortener/favicon.ico")
# root.geometry("400x200") 
root.config(background="#7397ce")
text_font = Font(size = 15)

url = StringVar()
url_address = StringVar()

def shortener():
    slink_screen.delete(0, END)
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copy_link():
    text = f"{slink_screen.get()}"
    copy = 'echo ' + text.strip() + '| clip'
    os.system(copy)

def clear():
    llink_screen.delete(0, END)
    

head_label = Label(root, text="Link Shortener!", bg="#7397ce")
section = Label(root, text="=================================================", bg="#7397ce")
llink_label = Label(root, text="Long URL: ", bg="#7397ce", fg="black")
llink_screen = Entry(root, textvariable=url, width=50, borderwidth=5)
slink_screen = Entry(root, textvariable=url_address, width=50, borderwidth=5)
shorten_btn = Button(root,  text="Shorten Link", padx=5, pady=5, bg="#7397ce", fg="black", command=shortener)
space = Label(root, text="=================================================", bg="#7397ce")
copy = Button(root, text="Copy", command = copy_link, padx=10, pady=5,bg="#7397ce", fg="black")
clear = Button(root, text="Clear", command = clear, padx=10, pady=5,bg="#7397ce", fg="black")

head_label.grid(column=0, row=0, columnspan=5)
llink_label.grid(column=2, row=2)
section.grid(row=1, columnspan=5)
llink_screen.grid(column=3, row=2)
shorten_btn.grid(column=0, row=4, columnspan=5)
space.grid(column=0, row=3, columnspan=5)
slink_screen.grid(column=0, columnspan=4, row=6)
space.grid(column=0, row=5, columnspan=5)
copy.grid(column=4, row=6)
clear.grid(column=4, row=2)

head_label["font"] = text_font

root.mainloop()