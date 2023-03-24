#this is a GUI calculater by EGOproject.
#credits:CODEMY.COM, EGOproject


from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("GUI EGOcalc")
root.iconbitmap("tkinter practice/GUI EGO programs/favicon/favicon.ico")

myfont = font.Font(size = 20)

calc_screen = Entry(root, width=40, borderwidth=1)
calc_screen.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

#when a button is clicked
def darkmode():
    mode = "dark"
    modes.moder(mode)

def lightmode():
    mode = "light"
    modes.moder(mode)

def button_click(number):
    current = calc_screen.get()
    calc_screen.delete(0, END)
    calc_screen.insert(0, str(current) + str(number))

def clear_screen():
    calc_screen.delete(0, END)
    
def button_plus():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "plus"
    num1 = float(first_number)
    calc_screen.delete(0, END)

def button_minus():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "minus"
    num1 = float(first_number)
    calc_screen.delete(0, END)

def button_times():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "times"
    num1 = float(first_number)
    calc_screen.delete(0, END)

def button_share():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "share"
    num1 = float(first_number)
    calc_screen.delete(0, END)

def button_square():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "square"
    num1 = float(first_number)
    calc_screen.delete(0, END)
    sq = num1*num1
    calc_screen.insert(0 , sq)

def button_sroot():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "sroot"
    num1 = float(first_number)
    calc_screen.delete(0, END)
    sqr = math.sqrt(num1)
    calc_screen.insert(0 , float(sqr))

def button_cube():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "cube"
    num1 = float(first_number)
    calc_screen.delete(0, END)
    cb = num1*num1*num1
    calc_screen.insert(0 , cb)

def button_croot():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "croot"
    num1 = float(first_number)
    calc_screen.delete(0, END)
    cbr = math.cbrt(num1)
    calc_screen.insert(0 , float(cbr))

def button_ans():
    second_number = calc_screen.get()
    calc_screen.delete(0, END)
    if operation == "plus":
        sum = num1 + float(second_number)
        calc_screen.insert(0 , sum)
    elif operation == "minus":
        diff = num1 - float(second_number)
        calc_screen.insert(0 , diff)
    elif operation == "times":
        prod = num1 * float(second_number)
        calc_screen.insert(0 , prod)
    elif operation == "share":
        quo = num1 / float(second_number)
        calc_screen.insert(0 , float(quo))
    


#buttons
class modes:
    def __init__(self, mode):
        self.mode = mode
    
    def moder (mode):
        if mode ==  "light":
            #number buttons
            modeb = Button(root, text = "Dark Mode", bg="black", fg="white", command=darkmode)
            button_1 = Button(root, text="1", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(1))
            button_2 = Button(root, text="2", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(2))
            button_3 = Button(root, text="3", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(3))
            button_4 = Button(root, text="4", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(4))
            button_5 = Button(root, text="5", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(5))
            button_6 = Button(root, text="6", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(6))
            button_7 = Button(root, text="7", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(7))
            button_8 = Button(root, text="8", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(8))
            button_9 = Button(root, text="9", bg="orangered", fg="white", padx=15, pady=5, command=lambda: button_click(9))
            button_0 = Button(root, text="0", bg="orangered", fg="white", padx=50, pady=-10, command=lambda: button_click(0))
            button_dec = Button(root, text=".", bg="orangered", fg="white", padx=19, pady=0, command=lambda: button_click("."))

            #function Buttons
            button_sq = Button(root, text="X²", bg="orange", fg="white", padx=9, pady=0, command=button_square, )
            button_sqr = Button(root, text="V2", bg="orange", fg="white", padx=7, pady=0, command=button_sroot)
            button_cb = Button(root, text="X³", bg="orange", fg="white", padx=9, pady=0, command=button_cube)
            button_cbr = Button(root, text="V3", bg="orange", fg="white", padx=7, pady=0, command=button_croot)
            button_equ = Button(root, text="=", bg="darkgreen", fg="white", padx=26, pady=47, command=button_ans)
            button_add = Button(root, text="+", bg="green", fg="white", padx=15, pady=36, command=button_plus)
            button_sub = Button(root, text="-", bg="green", fg="white", padx=19, pady=5, command=button_minus)
            button_mul = Button(root, text="X", bg="green", fg="white", padx=15, pady=5, command=button_times)
            button_div = Button(root, text="/", bg="green", fg="white", padx=19, pady=5, command=button_share)
            button_cls = Button(root, text="C", bg="maroon", fg="white", padx=12, pady=5, command=clear_screen)

            button_quit = Button(root, text="Exit EGOcalc", command=root.quit, bg="maroon", fg="white", padx=100, pady=0,)

            #font size
            button_sq["font"] = myfont
            button_sqr["font"] = myfont
            button_cb["font"] = myfont
            button_cbr["font"] = myfont
            button_div["font"] = myfont
            button_mul["font"] = myfont
            button_sub["font"] = myfont
            button_add["font"] = myfont
            button_cls["font"] = myfont
            button_0["font"] = myfont
            button_1["font"] = myfont
            button_2["font"] = myfont
            button_3["font"] = myfont
            button_4["font"] = myfont
            button_5["font"] = myfont
            button_6["font"] = myfont
            button_7["font"] = myfont
            button_8["font"] = myfont
            button_9["font"] = myfont
            button_dec["font"] = myfont

            #posting them to GUI
            button_0.grid(row=7, columnspan=2, column=0)

            button_1.grid(row=6, column=0)
            button_2.grid(row=6, column=1)
            button_3.grid(row=6, column=2)

            button_4.grid(row=5, column=0)
            button_5.grid(row=5, column=1)
            button_6.grid(row=5, column=2)

            button_7.grid(row=4, column=0)
            button_8.grid(row=4, column=1)
            button_9.grid(row=4, column=2)

            button_cls.grid(row=3, column=0)
            button_div.grid(row=3, column=1)
            button_mul.grid(row=3, column=2)
            button_sub.grid(row=3, column=3)
            button_add.grid(rowspan=2, row=4, column=3)
            button_equ.grid(rowspan=2, row=6, column=3)

            button_sq.grid(row=2, column=0)
            button_sqr.grid(row=2, column=1)
            button_cb.grid(row=2, column=2)
            button_cbr.grid(row=2, column=3)
            button_dec.grid(row=7, column=2)
            modeb.grid(row=0, column=3)

            button_quit.grid(row=8, columnspan=4)

        elif mode ==  "dark":
            #number buttons
            modeb = Button(root, text = "Light Mode", bg="white", fg="black", command=lightmode)
            button_1 = Button(root, text="1", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(1))
            button_2 = Button(root, text="2", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(2))
            button_3 = Button(root, text="3", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(3))
            button_4 = Button(root, text="4", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(4))
            button_5 = Button(root, text="5", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(5))
            button_6 = Button(root, text="6", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(6))
            button_7 = Button(root, text="7", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(7))
            button_8 = Button(root, text="8", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(8))
            button_9 = Button(root, text="9", bg="black", fg="white", padx=15, pady=5, command=lambda: button_click(9))
            button_0 = Button(root, text="0", bg="black", fg="white", padx=50, pady=-10, command=lambda: button_click(0))
            button_dec = Button(root, text=".", bg="black", fg="white", padx=19, pady=0, command=lambda: button_click("."))

            #function Buttons
            button_sq = Button(root, text="X²", bg="black", fg="white", padx=9, pady=0, command=button_square, )
            button_sqr = Button(root, text="V2", bg="black", fg="white", padx=7, pady=0, command=button_sroot)
            button_cb = Button(root, text="X³", bg="black", fg="white", padx=9, pady=0, command=button_cube)
            button_cbr = Button(root, text="V3", bg="black", fg="white", padx=7, pady=0, command=button_croot)
            button_equ = Button(root, text="=", bg="black", fg="white", padx=26, pady=47, command=button_ans)
            button_add = Button(root, text="+", bg="black", fg="white", padx=15, pady=36, command=button_plus)
            button_sub = Button(root, text="-", bg="black", fg="white", padx=19, pady=5, command=button_minus)
            button_mul = Button(root, text="X", bg="black", fg="white", padx=15, pady=5, command=button_times)
            button_div = Button(root, text="/", bg="black", fg="white", padx=19, pady=5, command=button_share)
            button_cls = Button(root, text="C", bg="black", fg="white", padx=12, pady=5, command=clear_screen)

            button_quit = Button(root, text="Exit EGOcalc", command=root.quit, bg="black", fg="white", padx=100, pady=0,)

            #font size
            button_sq["font"] = myfont
            button_sqr["font"] = myfont
            button_cb["font"] = myfont
            button_cbr["font"] = myfont
            button_div["font"] = myfont
            button_mul["font"] = myfont
            button_sub["font"] = myfont
            button_add["font"] = myfont
            button_cls["font"] = myfont
            button_0["font"] = myfont
            button_1["font"] = myfont
            button_2["font"] = myfont
            button_3["font"] = myfont
            button_4["font"] = myfont
            button_5["font"] = myfont
            button_6["font"] = myfont
            button_7["font"] = myfont
            button_8["font"] = myfont
            button_9["font"] = myfont
            button_dec["font"] = myfont

            #posting them to GUI
            button_0.grid(row=7, columnspan=2, column=0)

            button_1.grid(row=6, column=0)
            button_2.grid(row=6, column=1)
            button_3.grid(row=6, column=2)

            button_4.grid(row=5, column=0)
            button_5.grid(row=5, column=1)
            button_6.grid(row=5, column=2)

            button_7.grid(row=4, column=0)
            button_8.grid(row=4, column=1)
            button_9.grid(row=4, column=2)

            button_cls.grid(row=3, column=0)
            button_div.grid(row=3, column=1)
            button_mul.grid(row=3, column=2)
            button_sub.grid(row=3, column=3)
            button_add.grid(rowspan=2, row=4, column=3)
            button_equ.grid(rowspan=2, row=6, column=3)

            button_sq.grid(row=2, column=0)
            button_sqr.grid(row=2, column=1)
            button_cb.grid(row=2, column=2)
            button_cbr.grid(row=2, column=3)
            button_dec.grid(row=7, column=2)
            modeb.grid(row=0, column=3)

            button_quit.grid(row=8, columnspan=4)

lightmode()
root.mainloop()