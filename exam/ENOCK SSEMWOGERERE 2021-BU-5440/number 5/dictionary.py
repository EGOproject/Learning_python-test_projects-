# -*- coding: utf-8 -*-
"""
Created on Thu May 11 00:48:15 2023

@author: lab
"""


characters = []
frequency = []

print ("welcome to string frequence checker!!")
sentence = input("input your string!: ")

def checker():
    for c in sentence:
        if c not in characters:
            characters.append(c)
            f = sentence.count(c)
            frequency.append(f)
        
checker()

character_freqency = {"characters":frequency}
print(character_freqency)
        