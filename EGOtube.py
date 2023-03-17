# this is a simple program that can be used to download youtube videos
#credit to tuomaskijiova and patrickloeber

from pytube import YouTube
from tqdm import tqdm, trange
import time

print("Welcome to EGOtube")
print()
link = str(input("Paste the link: "))

eyt = YouTube(link)
print()
print("Video Title: ", eyt.title)
print("Video Views: ", eyt.views)

print()
print("Downloading...")

eyd = eyt.streams.get_highest_resolution()

eyd.download()

print("Compiling Resources...")

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.1)
        pbar.update(1)
print("Download Completed: ", eyd.download)



