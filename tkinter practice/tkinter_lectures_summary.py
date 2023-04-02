#credit:codemy.com for these lectures 
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

"""

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
def popup():
    messagebox.askyesnocancel("title of messagebox", "mesaage inside message box")

Button(root, text="popup", command=popup).pack()

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
# box.grid(row=0, column=0, sticky=W+E)

exit_button = Button(text="Exit", command=root.quit)
exit_button.pack()


root.mainloop()
radio=Tk()
radio.title("radio buttons")
radio.iconbitmap("tkinter practice/favicon/favicon.ico")

r = IntVar()
r.set("1")


Radiobutton(radio, text="option 1", variable=r, value=1).pack()
Radiobutton(radio, text="option 2", variable=r, value=2).pack()

radio.mainloop()
"""
#to use tkinter one should inport all its functions or methods
# every 

#tkinter works by  making an object and then posting it to the GUI

#title -- title widget
"""
root.title("actual title) names window title
"""
#grid vs pack
"""
---only one can be used at a time except when using frames.
---and also in flames one can be used at a time
---grid uses rows and columns while pack just packs the ocject in the particular space at that time.
pack example
    exit_button = Button(text="Exit", command=root.quit)
    exit_button.pack()
    orexit_button = Button(text="Exit", command=root.quit).pack()
grid example
    exit_button = Button(text="Exit", command=root.quit)
    exit_button.grid(row=1, column=1)
    orexit_button = Button(text="Exit", command=root.quit).grid(row=1, column=1)
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
---the tect section can be ignored when not needed
"""

#radio buttons
"""
r = IntVar() declare as integer variable
r.set("1") #to set the default
Radiobutton(root,text="option 1", variable=r, value=1).pack() 
"""

#message boxes
#tyupes of messageboxes
    #showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel
"""
from tkinter import messagebox

def popup():
    messagebox.showinfo("title of messagebox", "mesaageinside message box")

button(root, text="popup", command=popup).pack()
--- to get results
    Label(root,text=response).pack()
"""


#create new window
"""
first = Tk()
first.title("first window")
first.iconbitmap("tkinter practice/favicon/favicon.ico")

second = Tk()
second.title("second window")
second.iconbitmap("tkinter practice/favicon/favicon.ico")
Button(second, text="exit", command=second.destroy).pack()
#destroy only exits current window
first.mainloop()
"""

#create a file opening dialogue box
"""
root = Tk()
root.title("root window")
root.iconbitmap("tkinter practice/favicon/favicon.ico")
# from tkinter import filedialog
root.filename = filedialog.askopenfile(initialdir="G:\EGO archive\PYTHON\PRACTICE\practice\Learning_python-test_projects-\Learning_python-test_projects-\tkinter practice", title="open the file", filetypes=(("png files", "*.png"),("Icon files", "*.ico"),("All files", "*.*")))
fname = Label(root, text=root.filename).pack()
selected_image = ImageTk.PhotoImage(Image.open(root.filename))
img_label = Label(image=selected_image).pack()

root.mainloop()
"""

#navigation slider
"""
root = Tk()
root.title("slider ")
root.iconbitmap("tkinter practice/favicon/favicon.ico")

def slide(var):
    root.geometry(str(horizontal.get())+ "x" + str(vertical.get()))


vertical = Scale(root, from_=0, to=700, orient=VERTICAL, command = slide)
vertical.set(400)
vertical.pack()
horizontal= Scale(root, from_=0, to=600, orient=HORIZONTAL, command = slide)
horizontal.set(400)
horizontal.pack() 

root.mainloop()
"""

# check boxes
"""
root = Tk()
root.title("checkboxes ")
root.iconbitmap("tkinter practice/favicon/favicon.ico")


def show():
    label = Label(root, text=var.get()).pack()
var = StringVar()
check1 = Checkbutton(root, text="record steps", variable=var, onvalue="on", offvalue="off").pack()
Button(root, text="Recorder switch", command= show).pack()
#check1.diselect() to remove auto select
root.mainloop()
"""

#menu dropdown
"""
root = Tk()
root.title("menu dropdown ")
root.iconbitmap("tkinter practice/favicon/favicon.ico")

options = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
clicked = StringVar() 
clicked.set(options[4])

drop = OptionMenu(root, clicked, *options).pack()

root.mainloop()
"""

#using databases in python ---python SQL database
#import sqlite3
root = Tk()
root.title("databases ")
root.iconbitmap("tkinter practice/favicon/favicon.ico")

#Create a database or connect one
conn = sqlite3.connect("addressbook.db")

#create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE people(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        
        )""")
'''
def submit():
    conn = sqlite3.connect("addressbook.db")
    c = conn.cursor()

    c.execute("INSERT INTO people VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                "f_name": f_name_entry.get(),
                "l_name": l_name_entry.get(),
                "address": address_entry.get(),
                "city": city_entry.get(),
                "state": state_entry.get(),
                "zipcode": zipcode_entry.get(),
                # "comment": comment_entry.get
              })

    conn.commit()
    conn.close()




    f_name_entry.delete(0, END)
    l_name_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    # comment_entry.delete(0, END)

f_name_label = Label(root, text="First Name:").grid(row=0, column=0)
f_name_entry = Entry(root, width=30)
f_name_entry.grid(row=0, column=1)

l_name_label = Label(root, text="Last Name:").grid(row=1, column=0)
l_name_entry = Entry(root, width=30)
l_name_entry.grid(row=1, column=1)

address_label = Label(root, text="Address:").grid(row=2, column=0)
address_entry = Entry(root, width=30)
address_entry.grid(row=2, column=1)

city_label = Label(root, text="City:").grid(row=3, column=0)
city_entry = Entry(root, width=30)
city_entry.grid(row=3, column=1)

state_label = Label(root, text="State:").grid(row=4, column=0)
state_entry = Entry(root, width=30)
state_entry.grid(row=4, column=1)

zipcode_label = Label(root, text="Zip Code:").grid(row=5, column=0)
zipcode_entry = Entry(root, width=30)
zipcode_entry.grid(row=5, column=1)

# comment_label = Label(root, text="Comment:").grid(row=6, column=0)
# comment_entry = Entry(root, width=30,)
# comment_entry.grid(row=6, column=1)
 
Button(root, text="Add Record", command = submit).grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)
#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()