import pyautogui
import tkinter as tk
from tkinter.filedialog import *

# root = tk.Tk()

# layer = tk.Canvas(root, width=400, height=400)
# layer.pack()

def snap_screenshot():
    screen_snap = pyautogui.screenshot()
    save_path = asksaveasfilename()
    screen_snap.save(save_path+"_screenshot.png")

snap_screenshot()
# snap_button = tk.Button(text="Take screenshot", command=snap_screenshot, font=10)
# layer.create_window(160, 160, window=snap_button)

# root.mainloop()