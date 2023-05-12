# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:27:08 2023

@author: lab
"""
# a program that shows a list with stack properties

stack = [1,2,3,4,5,6,7,8,9]

# first in last out

def stack_list():
    stack.reverse()
    for num in stack:
        print(num)
stack_list()