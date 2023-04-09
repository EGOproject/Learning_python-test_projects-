#this is a tkinter music player.
# Credits: EGOproject

from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os


root = Tk()
root.title("Music Player")
root.resizable(False,False)
root.iconbitmap("tkinter practice/music player/favicon.ico")
root.config(background="#10004f")

mixer.init()

music_frame = Frame=(root, bd=2, relief=RIDGE)#this is the  space inside the frame
music_frame.pack(padx=400, pady=400, width=560, height=250 )

root.mainloop()