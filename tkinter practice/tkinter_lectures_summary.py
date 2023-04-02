from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Greeter")
root.iconbitmap("tkinter practice/favicon/favicon.ico")

my_font = font.Font(size=20)
button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

name = Entry(root, width=50, bg="teal", fg="white", borderwidth=5)
name.pack()
name.insert(0, "Enter name to Greet!!")
name.get()
box = Label(text= "anchor", bd=1, relief=SUNKEN, anchor=E)

pic = ImageTk.PhotoImage(Image.open("tkinter practice/favicon/android-chrome-512x512.png"))
pic_label = Label(image=pic)
number = 0
def onclick(number):
    number += 1
    myLabel = Label(root, text="Hello " + name.get() + f" 😁 {number}")
    myLabel.pack()
    pic_label.pack()
    button_quit.pack_forget()
    button_quit = Button(root, text="Exit program", command=root.quit, state=DISABLED)
    button_quit.pack()

my_button = Button(root, text="Greet", command=lambda: onclick(0), padx=10, pady = 1, fg="white", bg="black")
my_button["font"] = my_font
my_button.pack()
box.grid(row=0, column=0, sticky=W+E)

exit_button = Button(text="Exit", command=root.quit)
exit_button.pack()


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
for actual images
---from PIL import ImageTk, Image
    pic = ImageTk.PhotoImage(Image.open("tkinter practice/favicon/android-chrome-512x512.png"))
    pic_label = Label(image=pic)
    pic_label.pack() 
---to clear image from display, clear its location on the grid
    pic_label.grid_forget()
    OR
    button_quit.pack_forget()


"""
#buttons 2

"""
for the exit button
--button_quit = Button(root, command=root.quit)
--button_quit.pack()

--- to diable a button define its usual then mention the state as disabled
    button_quit = Button(root, text="Exit program", command=root.quit, state=DISABLED)
"""

#borders,allignment and apearance
"""
---for borders invoke the bd=border size required  
    name = Label(text= "name", bd=1)
---for apperance we invoke the relief attribute
    name = Label(text= "name", bd=1, relief=SUNKEN)
---for stetching the navigation of the content we invoke the sticky attribute while locating the lable on the gui and specify using initials of compass directions "NESW"
    name.grid(row=1, column=1, sticky= W+E)
---for allignment of the label or button we invoke the anchor attribute and give it a value to the direction we need it to be
    name = Label(text= "name", bd=1, relief=SUNKEN, anchor=E)
"""

#frames -- used to organise content in the root 
"""
frames =LabelFrame=(text="comment section", padx=1, pady=1)#this is the  space inside the frame
frame.pack(padx=1, pady=1)#this is the space arouns the frames
"""