# easy progress bar
#credits: Patrick Loeber, EGOproject

from tqdm import tqdm, trange
import time

with tqdm(total=100) as pbar:
    for i in range(1000):
        time .sleep(0.05)
        pbar.update(0.1)