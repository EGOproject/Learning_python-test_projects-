from tkinter import *
root = Tk()

def darkmode():
    mode = "dark"
    modes.moder(mode)

def lightmode():
    mode = "light"
    modes.moder(mode)

class modes:
    def __init__(self, mode):
        self.mode = mode
    
    def moder (mode):
        if mode ==  "dark":
            modeb = Button(root, text = "light mode", bg="white", fg="black", command=lightmode)
            yes = Button(root, text = "YES", bg="black", fg="white")
            no = Button(root, text = "NO", bg="black", fg="white")
            exit = Button(root, text = "EXIT", bg="black", fg="white")
            
            modeb.grid(row=0,column=3)
            yes.grid(row=1,column=0)
            no.grid(row=1,column=2)
            exit.grid(row=2,column=1)

        elif mode == "light":
            modeb = Button(root, text = "dark mode",bg="black", fg="white", command=darkmode)
            yes = Button(root, text = "YES", bg="orange", fg="white")
            no = Button(root, text = "NO", bg="orange", fg="white")
            exit = Button(root, text = "EXIT", bg="maroon", fg="white")


            modeb.grid(row=0,column=3)
            yes.grid(row=1,column=0)
            no.grid(row=1,column=2)
            exit.grid(row=2,column=1)
        else:
            pass

lightmode()
root.mainloop()