# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:09:48 2023

@author: lab
"""
import math

def factorial():
    num = int(input("Enter the number: "))
    result = math.factorial(num)
    print(num,"factorial is: ", result)
    
factorial()
