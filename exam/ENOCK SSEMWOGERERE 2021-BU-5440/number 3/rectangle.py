# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:37:11 2023

@author: lab
"""

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(length, width):
        r_area = length*width
        print("Area is: ", r_area, " square units")
        
        
length=int(input("Length of rectangle: "))
width = int(input("Width of rectangle: "))

result = Rectangle.area(length, width)