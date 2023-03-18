from tkinter import *

root = Tk()
root.title("Simple Greeter")

name = Entry(root, width=50, bg="teal", fg="white", borderwidth=5)
name.pack()
name.insert(0, "Enter name to Greet!!")
name.get()
 
def onclick():
    myLabel = Label(root, text="Hello " + name.get() + " 😁")
    myLabel.pack()

my_button = Button(root, text="Greet", command=onclick, padx=10, pady = 1, fg="white", bg="black")
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
"""

#input --- entry widget
"""
can modify its appearance
name.get() function grabs the input entered
name.insert() function creates a place holder for the input

"""