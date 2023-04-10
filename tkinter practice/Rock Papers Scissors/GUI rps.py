# this is the rock papers and scissors game that now has a GUI

from tkinter import *
import tkinter.font as font
import random
import pyttsx3
import time

root = Tk()
root.title("Rock PaperScissors")
root.iconbitmap("tkinter practice/Rock Papers Scissors/favicon.ico")
root.resizable(False,False)
root.config(background="#1e6c6c")
HEAD_font = font.Font(size = 20)
SIDE_font = font.Font(size = 16)
number_font = font.Font(size = 30)

cbg = "#1b428b"
ubg = "#508705"

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def selection(uv):
    cv = random.choice([1,2,3])

    if uv == cv:
        pyttsx3.speak("DRAW")
        # time.sleep(1)
    elif uv ==1:
        if uv == 1:
            if cv == 2:
                cw +=1
                ul +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("PAPER")
                # time.sleep(1)
            elif cv == 3:
                uw +=1
                cl +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("SCISSORS")
    elif uv ==2:
        if uv == 2:
            if cv == 1:
                uw +=1
                cl +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("ROCK")
                # time.sleep(1)

            elif cv == 3:
                cw +=1
                ul +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("SCISSORS")
                # time.sleep(1)
    elif uv == 3:
        if uv == 3:
            if cv == 1:
                cw +=1
                ul +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("ROCK")
                # time.sleep(1)
            elif cv == 2:
                uw +=1
                cl +=1
                us_string = f"      {uw}            {ul}"
                u_screen.delete(0, END)
                u_screen.insert(0, us_string)
                pyttsx3.speak("PAPER")
                # time.sleep(1)    

#   appearance of the gui
head_label = Label(root, text="ROCK PAPER SCISSORS", bg="#1e6c6c")
head_label.grid(row=0, column=0, columnspan = 6)
head_label["font"] = HEAD_font

U_label = Label(root, text="USER", bg=ubg)
U_label.grid(row=1, column=0, columnspan = 3, ipadx=110)
U_label["font"] = SIDE_font

rock_button = Button(root, text="💎", bg=ubg, command=lambda: selection(1))
rock_button.grid(row=2, column=0, padx=10,pady= 20)
paper_button = Button(root, text="📃", bg=ubg, command=lambda: selection(2))
paper_button.grid(row=2, column=1, padx=10,pady= 20)
scissor_button = Button(root, text="✂", bg=ubg, command=lambda: selection(3))
scissor_button.grid(row=2, column=2, padx=10,pady= 20)

rock_label = Label(root, text="ROCK", bg=ubg).grid(row=3, column=0, ipadx=25)
paper_label = Label(root, text="PAPER", bg=ubg).grid(row=3, column=1, ipadx=25)
scissor_label = Label(root, text="SCISSORS", bg=ubg).grid(row=3, column=2, ipadx=25)

#button fonts
rock_button["font"] = HEAD_font
paper_button["font"] = HEAD_font
scissor_button["font"] = HEAD_font

u_win_label = Label(root, text="WINS        LOSSES", bg=ubg)
u_win_label.grid(row=4, column=0, columnspan=3, ipadx=45,pady=5)
u_win_label["font"] = SIDE_font

u_screen = Entry(root, width=15)
u_screen.grid(row=5, column=0, columnspan=3)
u_screen["font"] =HEAD_font

root.mainloop()