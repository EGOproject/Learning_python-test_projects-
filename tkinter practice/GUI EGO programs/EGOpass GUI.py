from tkinter import *
from tkinter.font import  Font

root= Tk()
root.title("EGO Password Generator")
root.iconbitmap("tkinter practice/GUI EGO programs/favicon/favicon.ico")
root.geometry("400x400") 
text_font = Font(size = 20)

head_lable = Label(root, text="Password Requirements")
plen_label = Label(root, text="Password length" )

head_lable.grid(column=2, row=0)
plen_label.grid(column=0, row=1,rowspan=5)

root.mainloop()