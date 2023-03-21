from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Simple Greeter")
root.iconbitmap("tkinter practice/GUI EGOcalc/favicon/favicon.ico")

my_font = font.Font(size=20)
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

name = Entry(root, width=50, bg="teal", fg="white", borderwidth=5)
name.pack()
name.insert(0, "Enter name to Greet!!")
name.get()
 
def onclick(number):
    myLabel = Label(root, text="Hello " + name.get() + f" 😁 {number}")
    myLabel.pack()

my_button = Button(root, text="Greet", command=lambda: onclick(0), padx=10, pady = 1, fg="white", bg="black")
my_button["font"] = my_font
my_button.pack()

root.mainloop()


#to use tkinter one should inport all its functions or methods
# every 

#tkinter works by  making an object and then posting it to the GUI

#title -- title widget
"""
root.title("actual title) names window title
"""

#buttons--- button widget
"""
text = "button text"
command = name of function to perform when clicked
padx = padding x-axis
pady = padding y-axis
fg = button text color
bg = button color
command=lambda: button_click(1) = to pass a value from a button
for button text size
import tkinter.font as font
---create an object, name it(myFont) and do the following
    myFont = font.Font(size=15)
    my_button["font"] = myFont

"""

#input --- entry widget
"""
can modify its appearance
name.get() function grabs the input entered
name.insert() function creates a place holder for the input

"""

#images these are manipulated in the following ways.
"""
for icons
---root.iconbitmap("location of the image)
"""

#buttons 2

"""
for the exit button
--button_quit = Button(root, command=root.quit)
--button_quit.pack()
"""