# -*- coding: utf-8 -*-
"""
Created on Thu May 11 01:40:05 2023

@author: lab
"""

the_list = [1,1,5,7,8,5,2,3,1,9,7,5,6,1,2,4,5,7,8,6,3,9,8,2,5,1,4]
new_list = []

for i in the_list:
    if i not in new_list:
        new_list.append(i)
        
print(new_list)