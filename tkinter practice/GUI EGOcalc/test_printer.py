from tkinter import *
import win32ui 
text = """
    # easy progress bar\n
    #credits: Patrick Loeber, EGOproject\n

    from tqdm import tqdm, trange\n
    import time\n

    with tqdm(total=100) as pbar:\n
        for i in range(1000):\n
            time .sleep(0.05)\n
            pbar.update(0.1)
"""

dc = win32ui.CreateDC()
dc.CreatePrinterDC()
dc.StartDoc("my py document")

dc.StartPage()
dc.TextOut(100, 100, text)
dc.MoveTo(100, 102-200)
(0, 0)
dc.LineTo(200, 100)
dc.EndPage()

dc.EndDoc()