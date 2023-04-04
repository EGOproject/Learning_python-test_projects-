from pytube import YouTube
from tkinter import *
import tkxui

# root = tkxui.Tk(display=tkxui.FRAMELESS)
root = Tk()
# root.center()
root.resizable(False,False)
root.title("YouTube Max Video Downloader")
root.iconbitmap("tkinter practice/Youtube Downloader/favicon.ico")
root.config(background="#267573")

def clear():
    link_screen.delete(0, END)


def download():
    comment1 = "DOWNLOADING..."
    comment2 = "Download Complete!"
    link = link_screen.get()
    YouTube(link).streams.get_highest_resolution().download()
    link_screen.delete(0, END)
    link_screen.insert(0, comment2)

head_label = Label(root, text="Download Best Quality!", bg="#267573", fg="white").grid(row=0, column="0", columnspan=4, padx=10, pady=10)
link_label = Label(root, text="Paste Video URL: ", bg="#267573", fg="white").grid(row=1, column="0", padx=10, pady=10)
link_screen = Entry(root, width=30)
link_screen.grid(row=1, column="1", columnspan=2, padx=10, pady=10)
clear = Button(root, text="Clear", bg="#267573", fg="white", command=clear).grid(row=1, column=3, padx=10, pady=10)
download = Button(root, text="Download", command=download, bg="#267573", fg="white").grid(row=2, column=0, columnspan=4, padx=10, pady=10)

# link = input("Paste the Link")
# print("Downloading....")

# YouTube(link).streams.get_highest_resolution().download()
# print("Video Downloaded Sucessfully")

root.mainloop()