#this is  a digital clock 
#credits: EGOprojects


from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")
root.iconbitmap("tkinter practice/Digital Clock/favicon.ico")


def time():

    string1 = strftime("%A %D")
    labeld.config(text=string1)
    labeld.after(1000, time)

    string2 = strftime("%H:%M:%S")
    label.config(text=string2)
    label.after(1000, time)


labeld = Label(root, font=("ds-digital", 30), background="black", foreground="cyan")
labeld.pack(anchor='center')

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')
time()

mainloop()