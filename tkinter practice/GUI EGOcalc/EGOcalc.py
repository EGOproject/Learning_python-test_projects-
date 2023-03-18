#this is a GUI calculater by EGOproject.
#credits:CODEMY.COM, EGOproject


from tkinter import *
import math

root = Tk()
root.title("GUI EGOcalc")

calc_screen = Entry(root, width=40, borderwidth=5)
calc_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#when a button is clicked

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
    num1 = int(first_number)
    calc_screen.delete(0, END)

def button_minus():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "minus"
    num1 = int(first_number)
    calc_screen.delete(0, END)

def button_times():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "times"
    num1 = int(first_number)
    calc_screen.delete(0, END)

def button_share():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "share"
    num1 = int(first_number)
    calc_screen.delete(0, END)

def button_square():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "square"
    num1 = int(first_number)
    calc_screen.delete(0, END)
    sq = num1*num1
    calc_screen.insert(0 , sq)

def button_sroot():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "sroot"
    num1 = int(first_number)
    calc_screen.delete(0, END)
    sqr = math.sqrt(num1)
    calc_screen.insert(0 , int(sqr))

def button_cube():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "cube"
    num1 = int(first_number)
    calc_screen.delete(0, END)
    cb = num1*num1*num1
    calc_screen.insert(0 , cb)

def button_croot():
    first_number = calc_screen.get()
    global num1
    global operation
    operation = "croot"
    num1 = int(first_number)
    calc_screen.delete(0, END)
    cbr = math.cbrt(num1)
    calc_screen.insert(0 , int(cbr))

def button_ans():
    second_number = calc_screen.get()
    calc_screen.delete(0, END)
    if operation == "plus":
        sum = num1 + int(second_number)
        calc_screen.insert(0 , sum)
    elif operation == "minus":
        diff = num1 - int(second_number)
        calc_screen.insert(0 , diff)
    elif operation == "times":
        prod = num1 * int(second_number)
        calc_screen.insert(0 , prod)
    elif operation == "share":
        quo = num1 / int(second_number)
        calc_screen.insert(0 , int(quo))
    


#buttons
#number buttons
button_1 = Button(root, text="1", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="black", fg="white", padx=30, pady=15, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="black", fg="white", padx=105, pady=15, command=lambda: button_click(0))

#function Buttons
button_sq = Button(root, text="X²", bg="black", fg="yellow", padx=27, pady=15, command=button_square)
button_sqr = Button(root, text="²√", bg="black", fg="red", padx=27, pady=15, command=button_sroot)
button_cb = Button(root, text="X³", bg="black", fg="yellow", padx=27, pady=15, command=button_cube)
button_cbr = Button(root, text="³√", bg="black", fg="red", padx=27, pady=15, command=button_croot)
button_equ = Button(root, text="=", bg="green", fg="black", padx=30, pady=45, command=button_ans)
button_add = Button(root, text="➕", bg="gray", fg="blue", padx=25, pady=45, command=button_plus)
button_sub = Button(root, text="➖", bg="gray", fg="blue", padx=25, pady=15, command=button_minus)
button_mul = Button(root, text="✖", bg="gray", fg="blue", padx=25, pady=15, command=button_times)
button_div = Button(root, text="➗", bg="gray", fg="blue", padx=25, pady=15, command=button_share)
button_cls = Button(root, text="CLEAR", bg="red", fg="black", padx=15, pady=15, command=clear_screen)

#posting them to GUI
button_0.grid(row=6, columnspan=3, column=0)

button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_cls.grid(row=2, column=0)
button_div.grid(row=2, column=1)
button_mul.grid(row=2, column=2)
button_sub.grid(row=2, column=3)
button_add.grid(rowspan=2, row=3, column=3)
button_equ.grid(rowspan=2, row=5, column=3)

button_sq.grid(row=1, column=0)
button_sqr.grid(row=1, column=1)
button_cb.grid(row=1, column=2)
button_cbr.grid(row=1, column=3)
# button_dec.grid(row=5, column=2)

root.mainloop()