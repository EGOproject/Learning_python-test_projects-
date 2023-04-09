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

uw = 0
ul = 0

cw = 0
cl = 0

draws = 0

#logic of the game

uv =""
cv = ""


def win_draw_lose(player):
    if uv == cv:
        pass


#   appearance of the gui
head_label = Label(root, text="ROCK PAPER SCISSORS", bg="#1e6c6c")
head_label.grid(row=0, column=0, columnspan = 6)
head_label["font"] = HEAD_font

U_label = Label(root, text="USER", bg=ubg)
U_label.grid(row=1, column=0, columnspan = 3, ipadx=110)
U_label["font"] = SIDE_font

rock_button = Button(root, text="💎", bg=ubg)
rock_button.grid(row=2, column=0, padx=10,pady= 20)
paper_button = Button(root, text="📃", bg=ubg)
paper_button.grid(row=2, column=1, padx=10,pady= 20)
scissor_button = Button(root, text="✂", bg=ubg)
scissor_button.grid(row=2, column=2, padx=10,pady= 20)

rock_label = Label(root, text="ROCK", bg=ubg).grid(row=3, column=0, ipadx=25)
paper_label = Label(root, text="PAPER", bg=ubg).grid(row=3, column=1, ipadx=25)
scissor_label = Label(root, text="SCISSORS", bg=ubg).grid(row=3, column=2, ipadx=25)

u_win_label = Label(root, text="WINS        LOSSES", bg=ubg)
u_win_label.grid(row=4, column=0, columnspan=3, ipadx=45,pady=5)
u_win_label["font"] = SIDE_font

utstring = f"{uw}           {ul}"
uw_label = Label(root, text=utstring, fg="green")
uw_label.grid(row=5, column=0, columnspan=3, ipadx=30)
uw_label["font"] = number_font

# ul_label = Label(root, text=str(ul), fg="red")
# ul_label.grid(row=5, column=1, columnspan=2, ipadx=40)
# ul_label["font"] = number_font

#button fonts
rock_button["font"] = HEAD_font
paper_button["font"] = HEAD_font
scissor_button["font"] = HEAD_font

C_label = Label(root, text="COMPUTER", bg=cbg)
C_label.grid(row=1, column=3, columnspan = 3, ipadx=80)
C_label["font"] = SIDE_font


crock_button = Button(root, text="💎", bg=cbg)
crock_button.grid(row=2, column=3, padx=10,pady= 20)
cpaper_button = Button(root, text="📃", bg=cbg)
cpaper_button.grid(row=2, column=4, padx=10,pady= 20)
cscissor_button = Button(root, text="✂", bg=cbg)
cscissor_button.grid(row=2, column=5, padx=10,pady= 20)

rock_label = Label(root, text="ROCK", bg=cbg).grid(row=3, column=3, ipadx=25)
paper_label = Label(root, text="PAPER", bg=cbg).grid(row=3, column=4, ipadx=25)
scissor_label = Label(root, text="SCISSORS", bg=cbg).grid(row=3, column=5, ipadx=25)

c_win_label = Label(root, text="WINS        LOSSES", bg=cbg)
c_win_label.grid(row=4, column=3, columnspan=3, ipadx=45, pady=5)
c_win_label["font"] = SIDE_font

ctstring = f"{cw}           {cl}"
uw_label = Label(root, text=ctstring, fg="blue")
uw_label.grid(row=5, column=3, columnspan=3, ipadx=30)
uw_label["font"] = number_font

#button fonts
crock_button["font"] = HEAD_font
cpaper_button["font"] = HEAD_font
cscissor_button["font"] = HEAD_font

dtstring = f"{draws}    DRAWS"
draws_label = Label(root, text=dtstring)
draws_label.grid(row=6, column=0, columnspan=6, ipadx=5, pady=10)
draws_label["font"] = number_font

root.mainloop()