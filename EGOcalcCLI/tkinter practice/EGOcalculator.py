from tkinter import *

root = Tk()
root.title("GUI EGOcalc")

calc_screen = Entry(root, width=40, borderwidth=5)
calc_screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#when a button is clicked

def button_click(number):
    calc_screen.insert(0, number)
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
button_0 = Button(root, text="0", bg="black", fg="silver", padx=70, pady=15, command=lambda: button_click(0))

#function Buttons
button_dec = Button(root, text="•", bg="gray", fg="red", padx=30, pady=15, command=lambda: button_click())
button_equ = Button(root, text="=", bg="green", fg="black", padx=30, pady=45, command=lambda: button_click())
button_plus = Button(root, text="➕", bg="gray", fg="blue", padx=25, pady=45, command=lambda: button_click())
button_minus = Button(root, text="➖", bg="gray", fg="blue", padx=25, pady=15, command=lambda: button_click())
button_times = Button(root, text="✖", bg="gray", fg="blue", padx=25, pady=15, command=lambda: button_click())
button_div = Button(root, text="➗", bg="gray", fg="blue", padx=25, pady=15, command=lambda: button_click())
button_cls = Button(root, text="CLEAR", bg="red", fg="black", padx=15, pady=15, command=lambda: button_click())

#posting them to GUI
button_0.grid(row=5, columnspan=2, column=0)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_cls.grid(row=1, column=0)
button_div.grid(row=1, column=1)
button_times.grid(row=1, column=2)
button_minus.grid(row=1, column=3)
button_plus.grid(rowspan=2, row=2, column=3)
button_equ.grid(rowspan=2, row=4, column=3)
button_dec.grid(row=5, column=2)

root.mainloop()