#This is a tkinter project that can generate QRcodes
#credits: EGOprojet

from tkinter import *
from tkinter.filedialog import *
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

root = Tk()
root.title("QRcode Generator")
root.iconbitmap("tkinter practice/QRcode Generator/favicon.ico")
root.config(background="#267573")
root.resizable(False,False)

def clear():
    content_screen.delete(0, END)


def generate():
    qr = pyqrcode.create(content_screen.get())
    qr.png("QRCode.png", scale=8)
    

head_label = Label(root, text="Generate QRcode!", bg="#267573", fg="white").grid(row=0, column="0", columnspan=4, padx=10, pady=10)
content_label = Label(root, text="Paste Content: ", bg="#267573", fg="white").grid(row=1, column="0", padx=10, pady=10)
content_screen = Entry(root, width=30)
content_screen.grid(row=1, column="1", columnspan=2, padx=10, pady=10)
clear = Button(root, text="Clear", bg="#267573", fg="white", command=clear).grid(row=1, column=3, padx=10, pady=10)
generate = Button(root, text="Generate QRcode", command=generate, bg="#267573", fg="white").grid(row=2, column=0, columnspan=4, padx=10, pady=10)


root.mainloop()
# d = decode(Image.open("myCode.png"))
# print(d[0].data.decode("ascii"))